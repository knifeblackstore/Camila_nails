# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:


# Camila nails — Sitio web (React + Vite)

Proyecto frontend 100% en React para la marca "Camila nails". Incluye:

- Rutas para las secciones principales: Inicio, Historia, Estilos, Esmaltes, Enfermedades y Contacto.
- Inicio de sesión y registro (implementación sencilla con `localStorage`).
- Panel de administración local para autorizar cambios propuestos por usuarios.
- Formulario para agendar citas que redirige a WhatsApp con mensaje prellenado.

## Ejecutar en desarrollo

Instala dependencias y levanta el servidor de desarrollo:

```bash
npm install
npm run dev
```

La app quedará disponible por defecto en `http://localhost:5174/` (Vite puede asignar otro puerto si 5173 está en uso).

## Personalización rápida

- Número de WhatsApp: edita `src/pages/Contact.jsx` y modifica la constante `MANICURIST_PHONE` con el número en formato sin `+` ni prefijos (ej.: `573102864177`).
- Marca y título: `index.html` (título), y `src/components/Navbar.jsx` (texto de la marca) ya están configurados como "Camila nails".
- Administrador: para acceder al `AdminPanel`, inicia sesión con el email `admin@admin.com` o cualquier email que termine en `@admin`.

## Flujo de cambios y autorizaciones

- Los usuarios autenticados pueden "Proponer cambio" en secciones; las propuestas se guardan en `localStorage` bajo `kb_pending`.
- El administrador ve las propuestas en `AdminPanel` y puede aprobarlas (se mueven a `kb_approved`) o rechazarlas.

## Producción y siguientes pasos sugeridos

- Para producción, conecta el front con un backend real (API + base de datos) para autenticación, persistencia de cambios y roles seguros.
- Integrar una API de WhatsApp (ej. WhatsApp Business API) para confirmaciones automáticas.
- Añadir editor WYSIWYG para propuestas, subida de imágenes y sistema de notificaciones.

Si quieres, puedo:

- Configurar un backend mínimo para usuarios y aprobaciones.
- Añadir una galería de imágenes y ejemplo de contenido real para la sección de estilos.

---
Pequeña guía creada automáticamente para este proyecto. Si deseas que renombre la carpeta del proyecto o actualice metadatos adicionales, indícamelo y lo hago.
