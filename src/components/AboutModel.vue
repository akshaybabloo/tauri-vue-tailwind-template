<script setup lang="ts">
import { PhX } from "@phosphor-icons/vue";
import { onMounted, ref } from "vue";
import { invoke } from "@tauri-apps/api/core";

const model = defineModel("modelValue");
const version = ref<string | null>(null);

onMounted(async () => {
  version.value = await invoke("application_version");
});
</script>

<template>
  <div v-if="model" class="bg-gray-900/50 dark:bg-umbra/80 fixed inset-0 z-40">
    <div
      class="flex overflow-y-auto overflow-x-hidden fixed top-0 right-0 left-0 z-50 justify-center items-center w-full md:inset-0 h-[calc(100%-1rem)] max-h-full"
    >
      <div class="relative p-4 w-full max-w-md max-h-full">
        <div
          class="relative bg-white rounded-lg shadow-sm dark:bg-ebony border"
        >
          <button
            type="button"
            class="absolute top-3 end-2.5 text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm w-8 h-8 ms-auto inline-flex justify-center items-center dark:hover:bg-gray-600 dark:hover:text-white"
            data-modal-hide="popup-modal"
            @click="model = false"
          >
            <span><PhX size="20" /></span>
            <span class="sr-only">Close modal</span>
          </button>
          <div class="p-4 md:p-5 text-center">
            <img
              src="../assets/logo.png"
              class="mx-auto mb-4 w-12 h-12"
              alt="Logo"
            />
            <h3
              class="mb-5 text-lg font-normal text-gray-500 dark:text-gray-400"
            >
              About CiteMe
            </h3>
            <p>{{ version }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
