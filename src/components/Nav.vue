<script setup lang="ts">
import { onMounted, onUnmounted, ref } from "vue";
import { getCurrentWindow } from "@tauri-apps/api/window";
import { platform } from "@tauri-apps/plugin-os";
import { invoke } from "@tauri-apps/api/core";
import AboutModel from "./AboutModel.vue";
import WindowControls from "./WindowControls.vue";

const fileMenuDropdownOpen = ref(false);
const aboutMenuDropdownOpen = ref(false);
const isMaximized = ref(false);
const showAbout = ref(false);

const appWindow = getCurrentWindow();
const currentPlatform = platform();

// Function to close all dropdowns
const closeAllDropdowns = () => {
  fileMenuDropdownOpen.value = false;
  aboutMenuDropdownOpen.value = false;
};

const toggleDevTools = async () => {
  await invoke("toggle_devtools");
  closeAllDropdowns();
};

// Function to toggle a specific dropdown
const toggleDropdown = (dropdown: "file" | "about") => {
  if (dropdown === "file") {
    aboutMenuDropdownOpen.value = false;
    fileMenuDropdownOpen.value = !fileMenuDropdownOpen.value;
  } else {
    fileMenuDropdownOpen.value = false;
    aboutMenuDropdownOpen.value = !aboutMenuDropdownOpen.value;
  }
};

const handleMenuHover = (menu: "file" | "about") => {
  // Only switch if any menu is already open
  if (fileMenuDropdownOpen.value || aboutMenuDropdownOpen.value) {
    toggleDropdown(menu);
  }
};

// Click outside handler
const handleClickOutside = (event: MouseEvent) => {
  const target = event.target as HTMLElement;
  if (!target.closest(".dropdown-container")) {
    closeAllDropdowns();
  }
};

const openAboutModel = () => {
  showAbout.value = true;
  closeAllDropdowns();
};

// Lifecycle hooks for event listener
onMounted(async () => {
  document.addEventListener("click", handleClickOutside);
  console.debug("Platform = " + currentPlatform);

  isMaximized.value = await appWindow.isMaximized();
  await appWindow.onResized(async () => {
    isMaximized.value = await appWindow.isMaximized();
  });

  // TODO: Mac OS specific menu bar
});

onUnmounted(() => {
  document.removeEventListener("click", handleClickOutside);
});
</script>

<template>
  <nav data-tauri-drag-region class="bg-white border-gray-200 dark:bg-umbra border-b-[1px] border-b-ebony">
    <div data-tauri-drag-region class="w-auto flex flex-wrap items-center justify-between">
      <!--Close, Minimize, Maximize Buttons-->
      <WindowControls />

      <div class="items-center justify-between flex w-auto order-1 p-1">
        <ul class="flex font-normal p-0 space-x-2 flex-row mt-0 border-0 bg-white dark:bg-umbra dark:border-gray-700">
          <li>
            <img src="../assets/logo.png" class="ml-1 h-7" alt="CiteMe Logo" />
          </li>
          <!--File Menu-->
          <li class="relative dropdown-container">
            <button
              type="button"
              class="block py-1 px-2 text-sm text-umbra rounded dark:text-white dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
              @click.stop="toggleDropdown('file')"
              @mouseenter="handleMenuHover('file')"
              :class="fileMenuDropdownOpen ? 'bg-gray-100 dark:bg-gray-800' : ''"
            >
              File
            </button>

            <!--File Dropdown-->
            <div
              v-show="fileMenuDropdownOpen"
              class="absolute top-full left-0 z-50 font-normal bg-white divide-y divide-gray-100 rounded-sm shadow w-44 dark:bg-umbra dark:divide-gray-600 border border-gray-700"
            >
              <ul class="text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownLargeButton">
                <li>
                  <a
                    href="#"
                    @click="appWindow.close()"
                    class="block px-4 py-1 hover:rounded-sm hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
                    >Exit</a
                  >
                </li>
              </ul>
            </div>
          </li>

          <!--About Menu-->
          <li class="relative dropdown-container">
            <button
              type="button"
              class="block py-1 px-2 text-sm text-umbra rounded dark:text-white dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
              @click.stop="toggleDropdown('about')"
              @mouseenter="handleMenuHover('about')"
              :class="aboutMenuDropdownOpen ? 'bg-gray-100 dark:bg-gray-800' : ''"
            >
              Help
            </button>

            <!--About Dropdown-->
            <div
              v-show="aboutMenuDropdownOpen"
              class="absolute top-full left-0 z-50 font-normal bg-white divide-y divide-gray-100 rounded-sm shadow w-48 dark:bg-umbra dark:divide-gray-600 border border-gray-700"
            >
              <ul class="text-sm text-gray-700 dark:text-gray-200" aria-labelledby="dropdownLargeButton">
                <li>
                  <a
                    href="#"
                    @click="toggleDevTools"
                    class="block px-4 py-1 hover:rounded-sm hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
                    >Toggle Developer Tools</a
                  >
                </li>
                <li>
                  <hr class="h-px bg-gray-200 border-0 dark:bg-gray-700" />
                </li>
                <li>
                  <a
                    href="#"
                    @click="openAboutModel"
                    class="block w-auto px-4 py-1 hover:rounded-sm hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
                    >About</a
                  >
                </li>
              </ul>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </nav>

  <AboutModel v-model="showAbout" />
</template>

<style scoped></style>
