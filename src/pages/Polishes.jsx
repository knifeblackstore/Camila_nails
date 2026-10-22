// Catálogo de esmaltes con soporte para agregar esmaltes con foto y marcas
import React, { useContext, useEffect, useState } from 'react'
import { AuthContext } from '../AuthProvider'

const initialBrandGroups = [
  {
    title: 'Marcas populares y de uso local',
    brands: [
      { name: 'Masglo', description: 'Marca tradicional muy popular en Colombia, reconocida por su duración, sistema de pincel plano y esmaltes semipermanentes.' },
      { name: 'Vogue', description: 'Marca de alta disponibilidad en tiendas y farmacias locales, famosa por su línea de efecto gel y secado rápido.' },
      { name: 'Rimmel London', description: 'Ofrece opciones accesibles como la línea Super Gel.' },
      { name: 'Maybelline', description: 'Cuenta con esmaltes de secado rápido y gran variedad comercial.' },
    ],
  },
  {
    title: 'Marcas de gel semipermanente y caseras',
    brands: [
      { name: 'Beetles', description: 'Muy buscado en kits para principiantes y uso en casa con lámpara UV.' },
      { name: 'Semilac', description: 'Referente europeo en esmaltes permanentes de alta pigmentación.' },
      { name: 'Bluesky', description: 'Alternativa económica muy usada para manicura en gel.' },
      { name: 'Claresa', description: 'Alternativa económica muy usada para manicura en gel.' },
    ],
  },
]

export default function Polishes() {
  const { user } = useContext(AuthContext)
  const isAdmin = user?.role === 'admin' || user?.email === 'admin@admin.com'

  const [polishes, setPolishes] = useState([])
  const [showAddForm, setShowAddForm] = useState(false)
  const [name, setName] = useState('')
  const [brand, setBrand] = useState('')
  const [category, setCategory] = useState('Semipermanente')
  const [description, setDescription] = useState('')
  const [file, setFile] = useState(null)
  const [saving, setSaving] = useState(false)

  function loadPolishes() {
    fetch('/api/polishes')
      .then(r => r.json())
      .then(d => {
        if (Array.isArray(d)) setPolishes(d)
      })
      .catch(() => {})
  }

  useEffect(() => {
    loadPolishes()
  }, [])

  async function handleCreatePolish(e) {
    e.preventDefault()
    if (!name.trim()) return alert('El nombre del esmalte es obligatorio')

    setSaving(true)
    const form = new FormData()
    form.append('name', name)
    form.append('brand', brand)
    form.append('category', category)
    form.append('description', description)
    if (file) form.append('image', file)

    try {
      const res = await fetch('/api/polishes', {
        method: 'POST',
        body: form
      })
      const data = await res.json()
      if (!res.ok || !data.success) throw new Error(data.error || 'Error al guardar esmalte')

      setName('')
      setBrand('')
      setDescription('')
      setFile(null)
      setShowAddForm(false)
      loadPolishes()
      alert('¡Esmalte agregado con éxito!')
    } catch (err) {
      alert(err.message)
    } finally {
      setSaving(false)
    }
  }

  async function handleDeletePolish(id) {
    if (!window.confirm('¿Seguro que deseas eliminar este esmalte?')) return
    try {
      const res = await fetch(`/api/polishes/${id}`, { method: 'DELETE' })
      if (res.ok) loadPolishes()
    } catch (err) {
      alert('Error al eliminar')
    }
  }

  // Permite que el administrador actualice la descripción de una marca.
  function propose(b) {
    if (!user) return alert('Inicia sesión para proponer cambios')
    const t = window.prompt('Editar descripción de ' + b.name, b.description)
    if (t) {
      fetch('/api/pending', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ page: `polishes.${b.name}`, content: t, author: user.email || user.username }),
      })
        .then((r) => r.json())
        .then((d) => {
          if (d && d.success) alert('Enviado para autorización')
          else alert('Error: ' + (d.error || ''))
        })
        .catch(() => {
          const pending = JSON.parse(localStorage.getItem('kb_pending') || '[]')
          pending.push({ id: Date.now(), page: `polishes.${b.name}`, content: t, author: user.email || user.username, date: new Date().toISOString() })
          localStorage.setItem('kb_pending', JSON.stringify(pending))
          alert('Guardado localmente (offline)')
        })
    }
  }

  return (
    <section className="page polishes">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '15px', marginBottom: '20px' }}>
        <div>
          <h2>Esmaltes</h2>
          <p className="polishes-intro">Conoce nuestras marcas y colecciones de esmaltes con su respectiva foto y tonalidad.</p>
        </div>
        {isAdmin && (
          <button 
            type="button" 
            className="btn" 
            onClick={() => setShowAddForm(prev => !prev)}
            style={{ padding: '8px 18px', borderRadius: '20px' }}
          >
            {showAddForm ? '✕ Cerrar formulario' : '➕ Agregar esmalte con foto'}
          </button>
        )}
      </div>

      {showAddForm && isAdmin && (
        <form onSubmit={handleCreatePolish} className="custom-form" style={{ background: 'var(--surface-soft)', padding: '24px', borderRadius: '14px', border: '1px solid var(--border)', marginBottom: '30px', maxWidth: '600px', boxShadow: 'var(--shadow)' }}>
          <h3 style={{ marginTop: 0, marginBottom: '6px' }}>Nuevo Esmalte</h3>
          <p style={{ fontSize: '13px', color: 'var(--text-muted)', marginBottom: '16px' }}>Ingresa la información del esmalte junto con su muestra o fotografía:</p>

          <div className="custom-field">
            <label>Nombre o Tono del esmalte:</label>
            <input 
              type="text" 
              placeholder="Ej: Rojo Pasión #42" 
              value={name} 
              onChange={e => setName(e.target.value)} 
              required 
            />
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '15px' }}>
            <div className="custom-field">
              <label>Marca:</label>
              <input 
                type="text" 
                placeholder="Ej: Masglo, Semilac, Vogue" 
                value={brand} 
                onChange={e => setBrand(e.target.value)} 
              />
            </div>
            <div className="custom-field">
              <label>Tipo de esmalte:</label>
              <select value={category} onChange={e => setCategory(e.target.value)}>
                <option value="Semipermanente">Semipermanente</option>
                <option value="Tradicional">Tradicional</option>
                <option value="Gel UV">Gel UV</option>
                <option value="Rubber">Base Rubber</option>
                <option value="Glitter / Efecto">Glitter / Efecto Especial</option>
              </select>
            </div>
          </div>

          <div className="custom-field">
            <label>Descripción o recomendaciones:</label>
            <textarea 
              rows="2" 
              placeholder="Acabado mate, brillante, secado rápido, cobertura..." 
              value={description} 
              onChange={e => setDescription(e.target.value)} 
            />
          </div>

          <div className="custom-field">
            <label>Foto del esmalte o muestra de color:</label>
            <input 
              type="file" 
              accept="image/*" 
              onChange={e => setFile(e.target.files?.[0] || null)} 
            />
          </div>

          <button type="submit" className="btn" disabled={saving} style={{ marginTop: '10px', alignSelf: 'flex-start', padding: '10px 24px' }}>
            {saving ? 'Guardando esmalte...' : 'Guardar esmalte'}
          </button>
        </form>
      )}

      {/* Colección de esmaltes con foto */}
      {polishes.length > 0 && (
        <div style={{ marginBottom: '40px' }}>
          <h3 style={{ marginBottom: '15px' }}>Galería de Esmaltes Disponibles</h3>
          <div className="grid">
            {polishes.map((p) => (
              <article key={p.id} className="card" style={{ border: '1px solid var(--border)' }}>
                <div className="thumb">
                  {p.image_url ? (
                    <img src={p.image_url} alt={p.name} />
                  ) : (
                    <div style={{ height: '100%', display: 'flex', alignItems: 'center', justifyContent: 'center', background: 'var(--surface-muted)', color: 'var(--text-subtle)' }}>
                      💅 Sin foto
                    </div>
                  )}
                </div>
                <h3>{p.name}</h3>
                <div style={{ fontSize: '13px', fontWeight: 600, color: 'var(--accent)', marginBottom: '6px' }}>
                  {p.brand ? `${p.brand} · ` : ''}{p.category}
                </div>
                <p>{p.description}</p>
                {isAdmin && (
                  <button 
                    type="button" 
                    className="btn ghost tiny" 
                    onClick={() => handleDeletePolish(p.id)}
                    style={{ color: '#ef4444', borderColor: '#ef4444', marginTop: '12px' }}
                  >
                    🗑️ Eliminar esmalte
                  </button>
                )}
              </article>
            ))}
          </div>
        </div>
      )}

      {/* Marcas de esmaltes */}
      <h3 style={{ marginBottom: '15px' }}>Marcas de Referencia</h3>
      <div className="polish-groups">
        {initialBrandGroups.map((group) => (
          <section className="polish-group" key={group.title}>
            <h3>{group.title}</h3>
            <div className="polish-list">
              {group.brands.map((b) => (
                <article key={b.name} className="polish">
                  <strong>{b.name}</strong>
                  <p>{b.description}</p>
                  {isAdmin && <button className="btn tiny" onClick={() => propose(b)}>Editar</button>}
                </article>
              ))}
            </div>
          </section>
        ))}
      </div>
    </section>
  )
}
