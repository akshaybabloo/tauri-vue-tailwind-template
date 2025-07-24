<script setup lang="ts">
import { PhMinus, PhCopy, PhSquare, PhX } from '@phosphor-icons/vue'
import { onMounted, ref } from 'vue'
import { getCurrentWindow } from '@tauri-apps/api/window'
import { platform } from '@tauri-apps/plugin-os'

const isMaximized = ref(false)
const appWindow = getCurrentWindow()
const currentPlatform = platform()

// Lifecycle hooks for event listener
onMounted(async () => {
  console.log(currentPlatform)

  isMaximized.value = await appWindow.isMaximized()
  await appWindow.onResized(async () => {
    isMaximized.value = await appWindow.isMaximized()
  })
})
</script>

<template>
  <!--  Windows Controls-->
  <div class="flex order-2 space-x-0" v-if="currentPlatform === 'windows'">
    <ul class="flex font-normal p-0 flex-row mt-0 border-0 bg-base-100">
      <li>
        <div class="tooltip tooltip-bottom" data-tip="minimise">
          <button
            type="button"
            class="py-2 px-4 text-sm text-base-content hover:bg-base-300"
            @click="appWindow.minimize()"
          >
            <span><PhMinus size="20" /></span>
          </button>
        </div>
      </li>
      <li>
        <div class="tooltip tooltip-bottom !m-0 !p-0" data-tip="maximise">
          <button
            type="button"
            class="py-2 px-4 text-sm text-base-content hover:bg-base-300"
            @click="appWindow.toggleMaximize()"
          >
            <span v-if="isMaximized"><PhCopy size="20" /></span>
            <span v-else><PhSquare size="20" /></span>
          </button>
        </div>
      </li>
      <li>
        <div class="tooltip tooltip-bottom !m-0 !p-0" data-tip="close">
          <button
            type="button"
            class="py-2 px-4 text-sm m-0 text-base-content hover:bg-red-700"
            @click="appWindow.close()"
          >
            <span><PhX size="20" :class="isMaximized ? '' : 'ml-1'" /></span>
          </button>
        </div>
      </li>
    </ul>
  </div>

  <!--  Linux Controls-->
  <div class="flex order-2 space-x-0" v-if="currentPlatform === 'linux'">
    <ul class="flex font-normal p-0 flex-row mt-0 border-0 bg-base-100 gap-1 mr-1">
      <li>
        <div class="tooltip tooltip-bottom" data-tip="minimise">
          <button
            type="button"
            class="p-1 text-sm bg-gnome-controller text-base-content border-base-300 hover:bg-gnome-controller hover:brightness-125 hover:text-base-content rounded-full"
            @click="appWindow.minimize()"
          >
            <span><PhMinus size="15" /></span>
          </button>
        </div>
      </li>
      <li>
        <div class="tooltip tooltip-bottom !m-0 !p-0" data-tip="maximise">
          <button
            type="button"
            class="block p-1 text-sm bg-gnome-controller text-base-content border-base-300 hover:bg-gnome-controller hover:brightness-125 hover:text-base-content rounded-full"
            @click="appWindow.toggleMaximize()"
          >
            <span v-if="isMaximized"><PhCopy size="15" /></span>
            <span v-else><PhSquare size="15" /></span>
          </button>
        </div>
      </li>
      <li>
        <div class="tooltip tooltip-bottom !m-0 !p-0" data-tip="close">
          <button
            type="button"
            class="block p-1 text-sm bg-gnome-controller text-base-content border-base-300 hover:bg-gnome-controller hover:brightness-125 hover:text-base-content rounded-full"
            @click="appWindow.close()"
          >
            <span><PhX size="15" /></span>
          </button>
        </div>
      </li>
    </ul>
  </div>
</template>

<style scoped></style>
