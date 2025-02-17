<script setup lang="ts">
import Nav from "./components/nav/Nav.vue";
import FooterBar from "./components/FooterBar.vue";
</script>

<template>
  <div class="flex flex-col h-screen">
    <header class="fixed top-0 left-0 right-0 z-50 bg-base-100">
      <Nav />
    </header>
    <main class="flex-1 mt-7 mb-7 bg-base-200">
        <p>Your code here</p>
    </main>
    <footer class="fixed bottom-0 left-0 right-0 bg-base-100">
      <FooterBar data="" />
    </footer>
  </div>
</template>

<style scoped></style>
