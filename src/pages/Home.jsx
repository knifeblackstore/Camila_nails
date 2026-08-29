// Página principal con presentación del estudio, servicios y estilos destacados.
import React, { useContext, useEffect, useState } from 'react'
import { AuthContext } from '../AuthProvider'
import logo from '../assets/logo-camila-nails.png.jpeg'
import builderGelImage from '../assets/styles/builder-gel.jpg'
import rubberBaseImage from '../assets/styles/nivelacion-base-rubber.jpg'
import softGelImage from '../assets/styles/soft-gel.jpg'

  // Guarda una propuesta en el servidor o localmente cuando no hay conexión.
async function savePending(page, content, author) {
  try {
    const resp = await fetch('/api/pending', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ page, content, author }),
    })
    const data = await resp.json()
    if (resp.ok) return alert('Cambio enviado para autorización')
    return alert('Error enviando propuesta: ' + (data.error || 'error'))
  } catch (err) {
    // fallback to localStorage
    const pending = JSON.parse(localStorage.getItem('kb_pending') || '[]')
    pending.push({ id: Date.now(), page, content, author, date: new Date().toISOString() })
    localStorage.setItem('kb_pending', JSON.stringify(pending))
    alert('Cambio guardado localmente (offline)')
  }
}

export default function Home() {
  const { user } = useContext(AuthContext)
  const isAdmin = user?.role === 'admin' || user?.email === 'admin@admin.com'
  const [activeMood, setActiveMood] = useState('soft')
  const [isCarouselPaused, setIsCarouselPaused] = useState(false)
  const moodKeys = ['soft', 'bold', 'fresh']

  useEffect(() => {
    if (isCarouselPaused) return undefined
    const interval = window.setInterval(() => {
      setActiveMood((currentMood) => {
        const currentIndex = moodKeys.indexOf(currentMood)
        return moodKeys[(currentIndex + 1) % moodKeys.length]
      })
    }, 4500)
    return () => window.clearInterval(interval)
  }, [isCarouselPaused])

  const moods = {
    soft: {
      label: 'Soft gel',
      title: 'Delicada, pero imposible de ignorar.',
      detail: 'Brillos perlados, tonos lechosos y detalles que hablan bajito.',
      image: softGelImage,
      accent: 'Rosa nube',
    },
    bold: {
      label: 'Nivelación base rubber',
      title: 'Tu manicure también puede tener actitud.',
      detail: 'Tonos borgoña, brillo intenso y una forma que convierte cada gesto en look.',
      image: rubberBaseImage,
      accent: 'Borgoña',
    },
    fresh: {
      label: 'Builder gel',
      title: 'Un color nuevo para empezar de nuevo.',
      detail: 'French blanco, detalles florales y un acabado limpio para todos tus planes.',
      image: builderGelImage,
      accent: 'French floral',
    },
  }

  const mood = moods[activeMood]
  const featuredStyles = [
    { name: 'Builder gel', image: builderGelImage, detail: 'Estructura + resistencia' },
    { name: 'Nivelación base rubber', image: rubberBaseImage, detail: 'Natural + flexible' },
    { name: 'Soft gel', image: softGelImage, detail: 'Largo + ligero' },
  ]

  function edit() {
    if (!user) return alert('Inicia sesión para proponer cambios')
    const txt = window.prompt('Nuevo texto para la sección Hero', mood.title)
    if (txt) savePending('home.hero', txt, user.email || user.username)
  }

  return (
    <section className="home">
      <div className="home-kicker"><span /><img src={logo} alt="" /> Estudio de uñas & cuidado consciente <span /></div>

      <div className="hero-showcase">
        <div className="hero-copy">
          <p className="eyebrow">Camila nails / Pereira</p>
          <h1>Tu próxima <em>obsesión</em> empieza en tus manos.</h1>
          <p className="lead">Manicura creativa, asesoría cercana y diseños pensados para que te mires las manos todo el día.</p>
          <div className="hero-actions">
            <a href="/contact" className="btn btn-primary">Quiero mi cita <span>↗</span></a>
            <a href="/styles" className="text-link">Explorar estilos <span>→</span></a>
          </div>
          <div className="hero-proof"><strong>4.9</strong><span className="stars">★★★★★</span><span>+300 sets felices</span></div>
        </div>

        <div className={`hero-visual mood-visual-${activeMood}`} style={{ backgroundImage: `url(${mood.image})` }} onMouseEnter={() => setIsCarouselPaused(true)} onMouseLeave={() => setIsCarouselPaused(false)} onFocus={() => setIsCarouselPaused(true)} onBlur={() => setIsCarouselPaused(false)}>
          <div className="visual-tag">Inspiración del día <b>↗</b></div>
          <div className="visual-caption"><span>01</span><strong>{mood.label}</strong><small>{mood.accent} · Disponible esta semana</small></div>
        </div>
      </div>

      <div className="mood-picker" aria-label="Explora estilos por mood">
        <div className="mood-intro"><span>Elige tu mood</span><small>y mira qué aparece</small></div>
        <div className="mood-tabs">
          {Object.entries(moods).map(([key, value]) => (
            <button key={key} className={activeMood === key ? 'mood-tab active' : 'mood-tab'} onClick={() => setActiveMood(key)}>
              <span className={`mood-dot ${key}`} />{value.label}
            </button>
          ))}
        </div>
        <p className="mood-detail">{mood.title} <span>{mood.detail}</span></p>
      </div>

      <div className="home-signal-row">
        <div><span className="signal-number">01</span><strong>Diseño a tu medida</strong><p>No repetimos fórmulas: conversamos, diseñamos y creamos contigo.</p></div>
        <div><span className="signal-number">02</span><strong>Cuidado primero</strong><p>Herramientas esterilizadas y una guía honesta para tus uñas.</p></div>
        <div><span className="signal-number">03</span><strong>Tu momento favorito</strong><p>Un espacio para desconectar, elegir color y salir brillando.</p></div>
      </div>

      <div className="featured-styles">
        <div className="featured-heading"><div><p className="eyebrow">Lo que hacemos</p><h2>Encuentra tu próximo <em>set</em></h2></div><a href="/styles" className="text-link">Ver todos <span>→</span></a></div>
        <div className="featured-grid">
          {featuredStyles.map((style, index) => (
            <a href="/styles" className="featured-card" key={style.name}>
              <div className="featured-image"><img src={style.image} alt={style.name} /><span>0{index + 1}</span></div>
              <div className="featured-card-copy"><strong>{style.name}</strong><small>{style.detail}</small><b>↗</b></div>
            </a>
          ))}
        </div>
      </div>

      <div className="home-bottom-cta">
        <p>¿Ya sabes qué quieres?</p>
        <a href="/contact">Hablemos de tu próximo set <span>↗</span></a>
      </div>

      {isAdmin && <button className="edit-link" onClick={edit}>Editar contenido destacado</button>}
    </section>
  )
}
