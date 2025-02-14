use tauri::Manager;

#[cfg(target_os = "windows")]
use {
    tauri_plugin_positioner::{Position, WindowExt}
};

#[tauri::command]
fn application_version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

#[tauri::command]
fn toggle_devtools(window: tauri::Window) {
    let win = window.get_webview_window("main");

    if win.clone().unwrap().is_devtools_open() {
        win.unwrap().close_devtools();
    } else {
        win.unwrap().open_devtools();
    }
}

#[cfg_attr(mobile, tauri::mobile_entry_point)]
pub fn run() {
    tauri::Builder::default()
        .setup(|app| {
            #[cfg(desktop)]
            {
                app.handle()
                    .plugin(tauri_plugin_positioner::init())
                    .expect("TODO: panic message");
                tauri::tray::TrayIconBuilder::new()
                    .on_tray_icon_event(|tray_handle, event| {
                        tauri_plugin_positioner::on_tray_event(tray_handle.app_handle(), &event);
                    })
                    .build(app)?;

                // Set the window position to the top center of the screen
                let win = app.get_webview_window("main").unwrap();

                #[cfg(windows)]
                {
                    let _ = win.as_ref().window().move_window(Position::TopCenter);
                }
                win.set_shadow(true).expect("TODO: panic message");

                win.show().expect("Failed to show window");
            }

            Ok(())
        })
        .plugin(tauri_plugin_opener::init())
        .plugin(tauri_plugin_os::init())
        .plugin(tauri_plugin_shell::init())
        .invoke_handler(tauri::generate_handler![toggle_devtools, application_version])
        .run(tauri::generate_context!())
        .expect("error while running tauri application");
}
