import React, { useContext, useEffect, useState } from 'react'
import { AuthContext } from '../AuthProvider'
import Lightbox from '../components/Lightbox'

// Lista de condiciones con descripciones y ruta de imagen.
const initialDiseases = [
  {
    id: 'onicomicosis',
    name: 'Onicomicosis (Hongos)',
    desc: 'Uña amarilla, gruesa y deformada; ocasionada por infecciones fúngicas.',
    img: '/src/assets/diseases/1-onicomicosis.jpg',
  },
  {
    id: 'onicolisis',
    name: 'Onicólisis distal',
    desc: 'Uña desprendida del lecho ungueal, con separación en el borde distal.',
    img: '/src/assets/diseases/2-onicolisis.jpg',
  },
  {
    id: 'paroniquia',
    name: 'Paroniquia aguda',
    desc: 'Inflamación alrededor de la uña, a menudo con pus e infección bacteriana.',
    img: '/src/assets/diseases/3-paroniquia.jpg',
  },
  {
    id: 'onicocriptosis',
    name: 'Onicocriptosis (uñero)',
    desc: 'Uña clavada en la piel con dolor y posible sangrado o infección local.',
    img: '/src/assets/diseases/4-onicocriptosis.jpg',
  },
  {
    id: 'lineas-de-beau',
    name: 'Líneas de Beau',
    desc: 'Surcos transversales en la uña que indican trauma o interrupción temporal en la matriz.',
    img: '/src/assets/diseases/5-lineas-beau.jpg',
  },
  {
    id: 'leuconiquia',
    name: 'Leuconiquia punteada',
    desc: 'Manchas blancas puntiformes en la uña; suele estar relacionada con pequeños traumas.',
    img: '/src/assets/diseases/6-leuconiquia.jpg',
  },
  {
    id: 'uña-fragil',
    name: 'Síndrome de la uña frágil',
    desc: 'Uñas finas y quebradizas que se fragmentan con facilidad.',
    img: '/src/assets/diseases/7-una-fragil.jpg',
  },
  {
    id: 'psoriasis-ungueal',
    name: 'Psoriasis ungueal (Hoyuelos)',
    desc: 'Hoyuelos y depresiones en la lámina ungueal; asociado a psoriasis en piel.',
    img: '/src/assets/diseases/8-psoriasis.jpg',
  },
  {
    id: 'hematoma-subungueal',
    name: 'Hematoma subungueal',
    desc: 'Acumulación de sangre bajo la uña por traumatismo; coloración oscura o rojiza.',
    img: '/src/assets/diseases/9-hematoma.jpg',
  },
  {
    id: 'uña-verde',
    name: 'Síndrome de la uña verde (Pseudomonas)',
    desc: 'Coloración verdosa por infección bacteriana (pseudomonas) en ambientes húmedos.',
    img: '/src/assets/diseases/10-una-verde.jpg',
  },
]

export default function Diseases() {
  const { user } = useContext(AuthContext)
  const isAdmin = user?.role === 'admin' || user?.email === 'admin@admin.com'

  const [selected, setSelected] = useState(null)
  const [customDiseases, setCustomDiseases] = useState([])
  const [showAddForm, setShowAddForm] = useState(false)
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [recommendations, setRecommendations] = useState('')
  const [file, setFile] = useState(null)
  const [saving, setSaving] = useState(false)

  function loadDiseases() {
    fetch('/api/diseases')
      .then(r => r.json())
      .then(d => {
        if (Array.isArray(d)) setCustomDiseases(d)
      })
      .catch(() => {})
  }

  useEffect(() => {
    loadDiseases()
  }, [])

  async function handleCreateDisease(e) {
    e.preventDefault()
    if (!name.trim()) return alert('El nombre de la enfermedad o condición es obligatorio')

    setSaving(true)
    const form = new FormData()
    form.append('name', name)
    form.append('description', description)
    form.append('recommendations', recommendations)
    if (file) form.append('image', file)

    try {
      const res = await fetch('/api/diseases', {
        method: 'POST',
        body: form
      })
      const data = await res.json()
      if (!res.ok || !data.success) throw new Error(data.error || 'Error al guardar condición')

      setName('')
      setDescription('')
      setRecommendations('')
      setFile(null)
      setShowAddForm(false)
      loadDiseases()
      alert('¡Condición o enfermedad agregada con éxito!')
    } catch (err) {
      alert(err.message)
    } finally {
      setSaving(false)
    }
  }

  async function handleDeleteDisease(id) {
    if (!window.confirm('¿Seguro que deseas eliminar esta condición?')) return
    try {
      const res = await fetch(`/api/diseases/${id}`, { method: 'DELETE' })
      if (res.ok) loadDiseases()
    } catch (err) {
      alert('Error al eliminar')
    }
  }

  function open(d) { setSelected(d) }
  function close() { setSelected(null) }

  return (
    <section className="page diseases">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px', marginBottom: '20px' }}>
        <div>
          <h2>Guía de enfermedades y condiciones de las uñas</h2>
          <p style={{ color: 'var(--text-muted)' }}>Imágenes y descripciones de condiciones frecuentes. Haz clic en una tarjeta para ver más detalles.</p>
        </div>
        {isAdmin && (
          <button 
            type="button" 
            className="btn" 
            onClick={() => setShowAddForm(prev => !prev)}
            style={{ padding: '8px 18px', borderRadius: '20px' }}
          >
            {showAddForm ? '✕ Cerrar formulario' : '➕ Agregar nueva condición con foto'}
          </button>
        )}
      </div>

      {showAddForm && isAdmin && (
        <form onSubmit={handleCreateDisease} className="custom-form" style={{ background: 'var(--surface-soft)', padding: '24px', borderRadius: '14px', border: '1px solid var(--border)', marginBottom: '30px', maxWidth: '600px', boxShadow: 'var(--shadow)' }}>
          <h3 style={{ marginTop: 0, marginBottom: '6px' }}>Nueva Condición / Enfermedad</h3>
          <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '16px' }}>Registra una nueva afección de uñas para el catálogo formativo y preventivo:</p>

          <div className="custom-field">
            <label>Nombre de la condición:</label>
            <input 
              type="text" 
              placeholder="Ej: Anoniquia o Coiloniquia (Uñas en cuchara)" 
              value={name} 
              onChange={e => setName(e.target.value)} 
              required 
            />
          </div>

          <div className="custom-field">
            <label>Descripción y síntomas visuales:</label>
            <textarea 
              rows="3" 
              placeholder="Describe cómo se ve la uña, causas comunes y características..." 
              value={description} 
              onChange={e => setDescription(e.target.value)} 
            />
          </div>

          <div className="custom-field">
            <label>Recomendaciones o precauciones:</label>
            <textarea 
              rows="2" 
              placeholder="Ej: No realizar esmaltado semipermanente, remitir a dermatología..." 
              value={recommendations} 
              onChange={e => setRecommendations(e.target.value)} 
            />
          </div>

          <div className="custom-field">
            <label>Foto de la afección (opcional):</label>
            <input 
              type="file" 
              accept="image/*" 
              onChange={e => setFile(e.target.files?.[0] || null)} 
            />
          </div>

          <button type="submit" className="btn" disabled={saving} style={{ marginTop: '10px', alignSelf: 'flex-start', padding: '10px 24px' }}>
            {saving ? 'Guardando condición...' : 'Guardar condición'}
          </button>
        </form>
      )}

      <div className="diseases-grid">
        {/* Condiciones predeterminadas */}
        {initialDiseases.map((d) => (
          <article key={d.id} className="disease-card" role="button" tabIndex={0} onClick={() => open(d)} onKeyDown={(e) => { if (e.key === 'Enter') open(d) }}>
            <div className="disease-img-wrap">
              <img src={d.img} alt={d.name} onError={(e) => { e.currentTarget.style.display = 'none' }} />
              <div className="disease-placeholder">{d.name}</div>
            </div>

            <div className="disease-body">
              <h3>{d.name}</h3>
              <p>{d.desc}</p>
            </div>
          </article>
        ))}

        {/* Condiciones agregadas dinámicamente */}
        {customDiseases.map((cd) => {
          const itemForLightbox = {
            id: 'custom-' + cd.id,
            name: cd.name,
            desc: cd.description + (cd.recommendations ? `\n\nPrecaución: ${cd.recommendations}` : ''),
            img: cd.image_url
          }

          return (
            <article key={'cd-' + cd.id} className="disease-card" style={{ border: '1px solid var(--accent-border)' }}>
              <div className="disease-img-wrap" role="button" tabIndex={0} onClick={() => open(itemForLightbox)} style={{ cursor: 'pointer' }}>
                {cd.image_url ? (
                  <img src={cd.image_url} alt={cd.name} />
                ) : (
                  <div className="disease-placeholder">{cd.name}</div>
                )}
              </div>

              <div className="disease-body">
                <h3>{cd.name}</h3>
                <p>{cd.description}</p>
                {cd.recommendations && (
                  <small style={{ display: 'block', marginTop: '6px', color: 'var(--accent)' }}>
                    💡 {cd.recommendations}
                  </small>
                )}
                {isAdmin && (
                  <button 
                    type="button" 
                    className="btn ghost tiny" 
                    onClick={() => handleDeleteDisease(cd.id)}
                    style={{ color: '#ef4444', borderColor: '#ef4444', marginTop: '12px' }}
                  >
                    🗑️ Eliminar condición
                  </button>
                )}
              </div>
            </article>
          )
        })}
      </div>

      {/* Lightbox modal */}
      <Lightbox item={selected} onClose={close} />

      <h3 style={{ marginTop: '40px' }}>Consejos generales</h3>
      <ul>
        <li>Mantén las uñas limpias y secas para evitar infecciones.</li>
        <li>No cortes ni empujes cutículas agresivamente; usa herramientas esterilizadas.</li>
        <li>Consulta a un profesional ante dolor, cambio de color o secreción.</li>
        <li>Evita permanecer con las manos húmedas por períodos prolongados.</li>
      </ul>
    </section>
  )
}
