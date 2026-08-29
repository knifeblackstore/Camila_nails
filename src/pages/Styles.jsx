// Catálogo público de servicios y herramientas de edición exclusivas del admin.
import React, { useContext, useEffect, useState } from 'react'
import { AuthContext } from '../AuthProvider'
import builderGelImage from '../assets/styles/builder-gel.jpg'
import rubberBaseImage from '../assets/styles/nivelacion-base-rubber.jpg'
import softGelImage from '../assets/styles/soft-gel.jpg'
import semiPermanentImage from '../assets/styles/Esmaltado semipermanente.jpg'
import traditionalImage from '../assets/styles/Esmaltado tradicional.jpg'
import feetSemiPermanentImage from '../assets/styles/Semipermanente pies.jpg'

const stylesList = [
  { name: 'Builder gel', description: 'Refuerzo y estructura para uñas naturales, con un acabado resistente y elegante.', image: builderGelImage },
  { name: 'Nivelación base rubber', description: 'Base flexible que nivela la superficie y ayuda a proteger la uña natural.', image: rubberBaseImage },
  { name: 'Soft gel', description: 'Extensiones ligeras y cómodas para lucir el largo y la forma que prefieras.', image: softGelImage },
  { name: 'Esmaltado semipermanente', description: 'Color duradero con brillo intenso para mantener tus uñas impecables por más tiempo.', image: semiPermanentImage },
  { name: 'Esmaltado tradicional', description: 'Esmaltado clásico con el color y acabado que prefieras para una manicure sencilla.', image: traditionalImage },
  { name: 'Semipermanente pies', description: 'Color duradero y acabado impecable para lucir tus pies siempre arreglados.', image: feetSemiPermanentImage },
]

  // La vista pública usa imágenes predeterminadas o las subidas por el admin.
export default function Styles() {
  const { user } = useContext(AuthContext)
  const [uploadedImages, setUploadedImages] = useState({})
  const [uploadingStyle, setUploadingStyle] = useState('')
  const isAdmin = user?.role === 'admin' || user?.email === 'admin@admin.com'

  useEffect(() => {
    fetch('/api/uploads')
      .then((response) => response.json())
      .then((uploads) => {
        const images = {}
        uploads.forEach((upload) => {
          if (upload.style) images[upload.style] = upload.url
        })
        setUploadedImages(images)
      })
      .catch(() => setUploadedImages({}))
  }, [])

  async function uploadImage(styleName, event) {
    const file = event.target.files?.[0]
    event.target.value = ''
    if (!file) return

    setUploadingStyle(styleName)
    const form = new FormData()
    form.append('file', file)
    form.append('style', styleName)

    try {
      const response = await fetch('/api/upload', { method: 'POST', body: form })
      const data = await response.json()
      if (!response.ok || !data.success) throw new Error(data.error || 'No se pudo subir la imagen')
      setUploadedImages((current) => ({ ...current, [styleName]: data.url }))
    } catch (error) {
      alert(error.message)
    } finally {
      setUploadingStyle('')
    }
  }

  function propose(name) {
    if (!user) return alert('Inicia sesión para proponer cambios')
    const t = window.prompt('Sugerir detalle para ' + name, '')
    if (t) {
      fetch('/api/pending', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ page: `styles.${name}`, content: t, author: user.email || user.username }),
      })
        .then((r) => r.json())
        .then((d) => {
          if (d && d.success) alert('Enviado para autorización')
          else alert('Error: ' + (d.error || ''))
        })
        .catch(() => {
          const pending = JSON.parse(localStorage.getItem('kb_pending') || '[]')
          pending.push({ id: Date.now(), page: `styles.${name}`, content: t, author: user.email || user.username, date: new Date().toISOString() })
          localStorage.setItem('kb_pending', JSON.stringify(pending))
          alert('Guardado localmente (offline)')
        })
    }
  }

  return (
    <section className="page styles">
      <h2>Estilos de uñas</h2>
      <div className="grid">
        {stylesList.map((style) => (
          <article key={style.name} className="card">
            <div className="thumb">{(uploadedImages[style.name] || style.image) && <img src={uploadedImages[style.name] || style.image} alt={style.name} />}</div>
            <h3>{style.name}</h3>
            <p>{style.description}</p>
            {isAdmin && <label className="image-upload">
              <span>{uploadingStyle === style.name ? 'Subiendo...' : 'Agregar o cambiar foto'}</span>
              <input type="file" accept="image/*" onChange={(event) => uploadImage(style.name, event)} disabled={uploadingStyle !== ''} />
            </label>}
            {isAdmin && <button className="btn ghost" onClick={() => propose(style.name)}>Editar información</button>}
          </article>
        ))}
      </div>
    </section>
  )
}
