# Tauri 2 + Vue 3 + Tailwind 4 Starter Template

This is a template for building a desktop application using [Tauri](https://tauri.studio/), [Vue](https://vuejs.org/), and [Tailwind CSS](https://tailwindcss.com/).

It has a basic structure for running a Vue application inside a Tauri window.

## Features

- Title bar with minimize, maximize, and close buttons
- Frameless movable window
- File and Help menu with toggle dev tools

## Requirements

- [Node.js](https://nodejs.org/)
- [BunJs](https://bunjs.dev/)
- [UV](https://github.com/astral-sh/uv)

## Getting Started

1. Clone this repository
2. Install the dependencies
   ```bash
   bun install
   ```
3. Update the configuration by running
   ```bash
   uv run start.py
   ```
   Answer the questions to configure the application
4. Start the application
   ```bash
   bun run t:dev
   ```

### Further Customisation

To update the icons, replace `./app-icon.png` with your own image. And it must be a square image. Then run

```bash
bun run icon
```

This should generate the required icon files for the application.

## Thanks To

- [Application icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/application) For the application icon.
