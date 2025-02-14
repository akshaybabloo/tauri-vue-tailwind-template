<script setup lang="ts">
import { PhMinus, PhResize, PhSquare, PhX } from "@phosphor-icons/vue";
import { onMounted, ref } from "vue";
import { getCurrentWindow } from "@tauri-apps/api/window";
import { platform } from "@tauri-apps/plugin-os";

const isMaximized = ref(false);

const appWindow = getCurrentWindow();
const currentPlatform = platform();

// Lifecycle hooks for event listener
onMounted(async () => {
  console.log(currentPlatform);

  isMaximized.value = await appWindow.isMaximized();
  await appWindow.onResized(async () => {
    isMaximized.value = await appWindow.isMaximized();
  });

});
</script>

<template>
<!--  Windows Controls-->
  <div class="flex order-2 space-x-0" v-if="currentPlatform === 'windows'">
    <ul
      class="flex font-normal p-0 flex-row mt-0 border-0 bg-white dark:bg-umbra dark:border-gray-700"
    >
      <li>
        <button
          type="button"
          class="block py-2 px-2 text-sm text-umbra dark:text-white dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
          @click="appWindow.minimize()"
        >
          <span><PhMinus size="20" /></span>
        </button>
      </li>
      <li>
        <button
          type="button"
          class="block py-2 px-2 text-sm text-umbra dark:text-white dark:border-gray-700 hover:bg-gray-100 dark:hover:bg-gray-800 dark:hover:text-white"
          @click="appWindow.toggleMaximize()"
        >
          <span v-if="isMaximized"><PhResize size="20" /></span>
          <span v-else><PhSquare size="20" /></span>
        </button>
      </li>
      <li>
        <button
          type="button"
          class="block py-2 px-2 text-sm m-0 text-umbra dark:text-white dark:border-gray-700 hover:bg-red-700 dark:hover:text-white"
          :class="isMaximized ? '' : 'pr-4'"
          @click="appWindow.close()"
        >
          <span><PhX size="20" :class="isMaximized ? '' : 'ml-1'" /></span>
        </button>
      </li>
    </ul>
  </div>

<!--  Linux Controls-->
  <div class="flex order-2 space-x-0" v-if="currentPlatform === 'linux'">
    <ul
      class="flex font-normal p-0 flex-row mt-0 border-0 bg-white dark:bg-umbra dark:border-gray-700 gap-1 mr-1"
    >
      <li>
        <button
          type="button"
          class="block p-1 text-sm bg-gnome-controller text-white border-gray-700 hover:bg-gnome-controller hover:brightness-125 hover:text-white rounded-full"
          @click="appWindow.minimize()"
        >
          <span><PhMinus size="15" /></span>
        </button>
      </li>
      <li>
        <button
          type="button"
          class="block p-1 text-sm bg-gnome-controller text-white border-gray-700 hover:bg-gnome-controller hover:brightness-125 hover:text-white rounded-full"
          @click="appWindow.toggleMaximize()"
        >
          <span v-if="isMaximized"><PhResize size="15" /></span>
          <span v-else><PhSquare size="15" /></span>
        </button>
      </li>
      <li>
        <button
          type="button"
          class="block p-1 text-sm bg-gnome-controller text-white border-gray-700 hover:bg-gnome-controller hover:brightness-125 hover:text-white rounded-full"
          @click="appWindow.close()"
        >
          <span><PhX size="15" /></span>
        </button>
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>