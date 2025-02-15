<script setup lang="ts">
const props = defineProps<{
  data: string;
}>();
</script>

<template>
  <div
    class="fixed bottom-0 left-0 z-20 w-full p-1 bg-white border-t border-gray-200 shadow-sm dark:bg-umbra dark:border-ebony h-7"
  >
    <span class="text-xs text-gray-500 sm:text-center dark:text-gray-400">
      {{ props.data }}
    </span>
  </div>
</template>

<style scoped></style>
