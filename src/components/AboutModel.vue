<script setup lang="ts">
import { onMounted, ref } from "vue";
import { invoke } from "@tauri-apps/api/core";

const model = defineModel("modelValue");
const version = ref<string | null>(null);

onMounted(async () => {
  version.value = await invoke("application_version");
});
</script>

<template>
  <dialog id="my_modal_5" class="modal modal-bottom sm:modal-middle" :class="{ 'modal-open': model }">
    <div class="modal-box border border-base-300">
      <img src="../assets/logo.png" class="mx-auto mb-4 w-12 h-12" alt="Logo" />
      <h3 class="text-lg font-bold text-center">tauri-vue-tailwind-template</h3>
      <p class="py-4 text-center">Version: {{ version }}</p>
      <div class="modal-action">
        <form method="dialog">
          <button class="btn" @click="model = false">Close</button>
        </form>
      </div>
    </div>
  </dialog>
</template>
