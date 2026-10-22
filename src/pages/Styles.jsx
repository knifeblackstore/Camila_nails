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
  const [customStyles, setCustomStyles] = useState([])
  const [showAddForm, setShowAddForm] = useState(false)
  const [newStyleName, setNewStyleName] = useState('')
  const [newStyleDesc, setNewStyleDesc] = useState('')
  const [newStyleFile, setNewStyleFile] = useState(null)
  const [savingStyle, setSavingStyle] = useState(false)

  const isAdmin = user?.role === 'admin' || user?.email === 'admin@admin.com'

  function loadCustomStyles() {
    fetch('/api/custom-styles')
      .then(res => res.json())
      .then(data => {
        if (Array.isArray(data)) setCustomStyles(data)
      })
      .catch(() => {})
  }

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

    loadCustomStyles()
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

  async function handleCreateStyle(e) {
    e.preventDefault()
    if (!newStyleName.trim()) return alert('El nombre del estilo es obligatorio')

    setSavingStyle(true)
    const form = new FormData()
    form.append('name', newStyleName)
    form.append('description', newStyleDesc)
    if (newStyleFile) form.append('image', newStyleFile)

    try {
      const res = await fetch('/api/custom-styles', {
        method: 'POST',
        body: form
      })
      const data = await res.json()
      if (!res.ok || !data.success) throw new Error(data.error || 'Error al guardar')
      
      setNewStyleName('')
      setNewStyleDesc('')
      setNewStyleFile(null)
      setShowAddForm(false)
      loadCustomStyles()
      alert('¡Estilo agregado con éxito!')
    } catch (err) {
      alert(err.message)
    } finally {
      setSavingStyle(false)
    }
  }

  async function handleDeleteCustomStyle(id) {
    if (!window.confirm('¿Seguro que deseas eliminar este estilo?')) return
    try {
      const res = await fetch(`/api/custom-styles/${id}`, { method: 'DELETE' })
      if (res.ok) loadCustomStyles()
    } catch (err) {
      alert('Error al eliminar')
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
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px', marginBottom: '20px' }}>
        <div>
          <h2>Estilos de uñas</h2>
          <p style={{ color: 'var(--text-muted)' }}>Descubre nuestra variedad de técnicas y estilos para el cuidado y embellecimiento de tus manos y pies.</p>
        </div>
        {isAdmin && (
          <button 
            type="button" 
            className="btn" 
            onClick={() => setShowAddForm(prev => !prev)}
            style={{ padding: '8px 18px', borderRadius: '20px' }}
          >
            {showAddForm ? '✕ Cerrar formulario' : '➕ Agregar nuevo estilo'}
          </button>
        )}
      </div>

      {showAddForm && isAdmin && (
        <form onSubmit={handleCreateStyle} className="custom-form" style={{ background: 'var(--surface-soft)', padding: '24px', borderRadius: '14px', border: '1px solid var(--border)', marginBottom: '30px', maxWidth: '600px', boxShadow: 'var(--shadow)' }}>
          <h3 style={{ marginTop: 0, marginBottom: '6px' }}>Agregar nuevo estilo de uñas</h3>
          <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '16px' }}>Completa los campos a continuación para publicar un nuevo estilo o técnica en el catálogo:</p>
          
          <div className="custom-field">
            <label>Nombre del estilo o servicio:</label>
            <input 
              type="text" 
              placeholder="Ej: Uñas Acrílicas Esculpidas" 
              value={newStyleName} 
              onChange={e => setNewStyleName(e.target.value)} 
              required 
            />
          </div>

          <div className="custom-field">
            <label>Descripción del procedimiento:</label>
            <textarea 
              rows="3" 
              placeholder="Explica en qué consiste el procedimiento, materiales y su acabado..." 
              value={newStyleDesc} 
              onChange={e => setNewStyleDesc(e.target.value)} 
            />
          </div>

          <div className="custom-field">
            <label>Foto del estilo (opcional):</label>
            <input 
              type="file" 
              accept="image/*" 
              onChange={e => setNewStyleFile(e.target.files?.[0] || null)} 
            />
          </div>

          <button type="submit" className="btn" disabled={savingStyle} style={{ marginTop: '10px', alignSelf: 'flex-start', padding: '10px 24px' }}>
            {savingStyle ? 'Guardando estilo...' : 'Guardar estilo'}
          </button>
        </form>
      )}

      <div className="grid">
        {/* Estilos predeterminados */}
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

        {/* Estilos nuevos agregados por el usuario */}
        {customStyles.map((cs) => (
          <article key={'custom-' + cs.id} className="card" style={{ border: '1px solid var(--accent-border)' }}>
            <div className="thumb">
              {cs.image_url ? (
                <img src={cs.image_url} alt={cs.name} />
              ) : (
                <div style={{ height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'var(--surface-muted)', color: 'var(--text-subtle)' }}>
                  Sin imagen
                </div>
              )}
            </div>
            <h3>{cs.name}</h3>
            <p>{cs.description}</p>
            {isAdmin && (
              <button 
                type="button" 
                className="btn ghost tiny" 
                onClick={() => handleDeleteCustomStyle(cs.id)}
                style={{ color: '#ef4444', borderColor: '#ef4444', marginTop: '10px' }}
              >
                🗑️ Eliminar estilo
              </button>
            )}
          </article>
        ))}
      </div>
    </section>
  )
}
