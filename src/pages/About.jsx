// Página pública con la historia y los datos profesionales de Camila Nails.
import React, { useContext } from 'react'
import { AuthContext } from '../AuthProvider'
import profileImage from '../assets/about/maria-camila-alvarez-correa.jpg'

export default function About() {
  const { user } = useContext(AuthContext)
  const isAdmin = user?.role === 'admin' || user?.email === 'admin@admin.com'

  // Permite al administrador enviar una modificación para aprobación.
  function propose() {
    if (!user) return alert('Inicia sesión para proponer cambios')
    const t = window.prompt('Editar historia de la manicurista', 'Historia...')
    if (t) {
      fetch('/api/pending', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ page: 'about.history', content: t, author: user.email || user.username }),
      })
        .then((r) => r.json())
        .then((d) => {
          if (d && d.success) alert('Cambio enviado para autorización')
          else alert('Error enviando: ' + (d.error || ''))
        })
        .catch(() => {
          const pending = JSON.parse(localStorage.getItem('kb_pending') || '[]')
          pending.push({ id: Date.now(), page: 'about.history', content: t, author: user.email || user.username, date: new Date().toISOString() })
          localStorage.setItem('kb_pending', JSON.stringify(pending))
          alert('Cambio guardado localmente (offline)')
        })
    }
  }

  return (
    <section className="content page-about">
      <h2>Historia de la manicurista</h2>
      <div className="about-profile">
        <div className="about-profile-visual" aria-label="Foto de María Camila">
          <img src={profileImage} alt="María Camila Álvarez Correa" />
        </div>
        <div className="about-profile-copy">
          <p className="eyebrow">Camila nails / Pereira, Risaralda</p>
          <h3>María Camila Álvarez Correa</h3>
          <p>
            Tengo 31 años y me dedico al cuidado y embellecimiento de manos y pies,
            creando servicios personalizados para que cada cliente se sienta cómoda,
            segura y feliz con sus uñas.
          </p>
          <p>
            Mi formación es como <strong>Operaria en cuidado estético de manos y pies</strong>,
            con pasión por los detalles, la limpieza y las técnicas que ayudan a
            mantener unas uñas bonitas y saludables.
          </p>
        </div>
      </div>

      <div className="about-details">
        <div><span>Formación</span><strong>Operaria en cuidado estético de manos y pies</strong></div>
        <div><span>Ubicación</span><strong>Pereira, Risaralda</strong><small>Barrio Luis Alberto Duque</small></div>
        <div><span>Contacto</span><a href="tel:3102864177">310 286 4177</a><a href="mailto:camila__275@hotmail.com">camila__275@hotmail.com</a></div>
        <div><span>Instagram</span><a href="https://instagram.com/camila_nails0311" target="_blank" rel="noreferrer">@camila_nails0311</a></div>
      </div>
      {isAdmin && <button className="btn ghost" onClick={propose}>Editar historia</button>}
    </section>
  )
}
