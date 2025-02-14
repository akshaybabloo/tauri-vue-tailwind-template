import json
from pathlib import Path
from pydantic import BaseModel, field_validator, ValidationError
from rich.console import Console

CWD = Path(__file__).parent


class Questions(BaseModel):
    """
    Pydantic model for the questions asked in the setup wizard.
    """
    title: str
    product_name: str
    identifier: str
    author: str
    description: str = ""

    @field_validator("product_name", mode="after")
    @classmethod
    def no_spaces_or_special_characters(cls, value: str) -> str:
        """
        Checks if the product name and identifier contain spaces or special characters.
        """
        if not any(char in value for char in " !@#$%^&*()+={[}]|\\:;\"'<,>.?/~`"):
            return value
        raise ValueError("Product name and identifier must not contain spaces or special characters.")

    @field_validator("identifier", mode="after")
    @classmethod
    def identifier_starts_with_com(cls, value: str) -> str:
        """
        Checks if the identifier starts with 'com.'.
        """
        if value.startswith("com."):
            return value
        raise ValueError("Identifier must start with 'com.'.")

    @field_validator("product_name", "identifier", "author", mode="after")
    @classmethod
    def non_empty_string(cls, value: str) -> str:
        """
        Checks if the value is a non-empty string.
        """
        if value:
            return value
        raise ValueError("Value must not be empty.")


def questions() -> Questions:
    """
    Asks the user for the project title, product name and identifier.
    """
    console = Console(style="green")
    console.print("Welcome to the setup wizard!")
    console.print("Please answer the following questions to configure your project. \n")

    title = console.input("What is the title of your project? (e.g. My Project)\n> ")
    description = console.input("Please enter a description for your project\n> ")
    product_name = console.input("What is the name of your product? (e.g. my-project)\n> ")
    identifier = console.input("What is the identifier of your product? (e.g. com.example.my-project)\n> ")
    author = console.input("What is your name? (e.g. John Doe <john.doe@example.com>)\n> ")

    return Questions(title=title, product_name=product_name, identifier=identifier, author=author,
                     description=description)


def update_tauri_config(q: Questions):
    """
    Updates the TAURI configuration file with the user's answers.
    """
    tauri_config_path = Path(CWD).joinpath("src-tauri", "tauri.conf.json")
    rust_project_path = Path(CWD).joinpath("src-tauri", "Cargo.toml")
    main_rs_path = Path(CWD).joinpath("src-tauri", "src", "main.rs")

    with open(tauri_config_path, "r") as f:
        tauri_config = json.load(f)

    tauri_config["productName"] = q.product_name
    tauri_config["identifier"] = q.identifier
    tauri_config["app"]["windows"][0]["title"] = q.title

    with open(tauri_config_path, "w", encoding="utf-8") as f:
        json.dump(tauri_config, f, indent=2)

    # Read Cargo.toml into memory
    with open(rust_project_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Modify necessary lines
    for i, line in enumerate(lines):
        if line.startswith("name") and "_lib" not in line and "#" not in line:
            lines[i] = f'name = "{q.product_name}"\n'
        if line.startswith("description"):
            lines[i] = f'description = "{q.description}"\n'
        if line.startswith("authors"):
            lines[i] = f'authors = ["{q.author}"]\n'
        if line.startswith("name") and "_lib" in line and "#" not in line:
            lines[i] = f'name = "{q.product_name.replace("-", "_")}_lib"\n'

    # Write back modified TOML file
    with open(rust_project_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    # Modify main.rs file
    with open(main_rs_path, "r", encoding="utf-8") as f:
        lines = f.read()

    lines = lines.replace("tauri_app_lib", f"{q.product_name.replace('-', '_')}_lib")

    with open(main_rs_path, "w", encoding="utf-8") as f:
        f.write(lines)


if __name__ == "__main__":
    try:
        q = questions()
    except ValidationError as e:
        console = Console(style="red")
        console.print(f"\n[bold red]Error:[/bold red] {e.errors()[0]['msg']}\n")
        console.print("\n[bold red]Please try again.[/bold red]")
        exit(1)

    update_tauri_config(q)
