<script setup lang="ts">
const props = defineProps<{
  data: string;
}>();
</script>

<template>
  <div
    class="fixed bottom-0 left-0 z-20 w-full p-1 bg-base-100 border-t border-base-300 shadow-sm dark:bg-base-100 dark:border-base-300 h-7"
  >
    <span class="text-xs text-base-200 sm:text-center dark:text-base-200">
      {{ props.data }}
    </span>
  </div>
</template>

<style scoped></style>
