// Configuración de Vite, React y el proxy hacia el servidor local.
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Define los plugins y redirige las peticiones de API al backend.
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': 'http://localhost:4000',
      '/uploads': 'http://localhost:4000',
    },
  },
})
