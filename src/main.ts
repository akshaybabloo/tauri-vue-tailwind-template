import { createApp } from 'vue'
import App from './App.vue'

import './assets/main.css'

// Prevent right-click context menu
document.addEventListener('contextmenu', (event) => {
  event.preventDefault()
})

createApp(App).mount('#app')
