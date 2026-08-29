import { useContext, useEffect, useState } from 'react'
import { AuthContext } from '../AuthProvider'

const initialForm = {
  nombre: '',
  telefono: '',
  servicio: 'Builder gel',
  estado_actual: 'Normal',
  alergias: '',
  enfermedades: '',
  historial: '',
  preferencia: '',
  observaciones: '',
}

export default function FichaTecnica() {
  const { user } = useContext(AuthContext)
  const [form, setForm] = useState(initialForm)
  const [savedEntries, setSavedEntries] = useState([])
  const [loading, setLoading] = useState(false)

  useEffect(() => {
    if (!user) return
    async function load() {
      try {
        const res = await fetch('/api/fichas')
        const data = await res.json()
        const mine = (data || []).filter((item) => String(item.userId) === String(user.id) || item.email === user.email)
        setSavedEntries(mine)
      } catch (err) {
        setSavedEntries([])
      }
    }
    load()
  }, [user])

  function handleChange(event) {
    const { name, value } = event.target
    setForm((current) => ({ ...current, [name]: value }))
  }

  async function handleSubmit(event) {
    event.preventDefault()
    if (!user) return

    setLoading(true)
    try {
      const res = await fetch('/api/fichas', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          ...form,
          userId: user.id,
          username: user.username,
          email: user.email,
        }),
      })

      const data = await res.json()
      if (!res.ok) {
        alert(data.error || 'No se pudo guardar la ficha')
        return
      }

      setForm(initialForm)
      const resList = await fetch('/api/fichas')
      const list = await resList.json()
      const mine = (list || []).filter((item) => String(item.userId) === String(user.id) || item.email === user.email)
      setSavedEntries(mine)
      alert('Ficha técnica guardada correctamente')
    } catch (err) {
      alert('Error al guardar la ficha técnica')
    } finally {
      setLoading(false)
    }
  }

  return (
    <section className="page ficha-shell">
      <div className="ficha-card">
        <div className="ficha-header">
          <p className="eyebrow">Tu información</p>
          <h2>Ficha técnica</h2>
        </div>

        <p className="ficha-intro">Completa esta información para ayudarnos a preparar tu cita con más precisión.</p>

        <form onSubmit={handleSubmit} className="ficha-form">
          <div className="ficha-grid">
            <label>
              <span>Nombre</span>
              <input name="nombre" value={form.nombre} onChange={handleChange} placeholder="Tu nombre" required />
            </label>
            <label>
              <span>Teléfono</span>
              <input name="telefono" value={form.telefono} onChange={handleChange} placeholder="Número de contacto" required />
            </label>
          </div>

          <div className="ficha-grid">
            <label>
              <span>Servicio solicitado</span>
              <select name="servicio" value={form.servicio} onChange={handleChange}>
                <option>Builder gel</option>
                <option>Nivelación base rubber</option>
                <option>Soft gel</option>
                <option>Esmaltado semipermanente</option>
                <option>Esmaltado tradicional</option>
                <option>Semipermanente pies</option>
              </select>
            </label>

            <label>
              <span>Estado actual de las uñas</span>
              <select name="estado_actual" value={form.estado_actual} onChange={handleChange}>
                <option>Normal</option>
                <option>Débiles</option>
                <option>Escamadas</option>
                <option>Muy cortas</option>
                <option>Con levantamiento</option>
              </select>
            </label>
          </div>

          <label>
            <span>¿Tienes alergias o sensibilidad a algún producto?</span>
            <textarea name="alergias" value={form.alergias} onChange={handleChange} rows="3" placeholder="Ej: alergia al acetato, productos con fragancia..." />
          </label>

          <label>
            <span>Enfermedades, condiciones o tratamientos actuales</span>
            <textarea name="enfermedades" value={form.enfermedades} onChange={handleChange} rows="3" placeholder="Ej: diabetes, tiroides, uñas quebradizas..." />
          </label>

          <label>
            <span>Historial de manicura / uñas</span>
            <textarea name="historial" value={form.historial} onChange={handleChange} rows="3" placeholder="Cuéntanos tu experiencia reciente" />
          </label>

          <label>
            <span>Preferencias de estilo o color</span>
            <textarea name="preferencia" value={form.preferencia} onChange={handleChange} rows="3" placeholder="Forma, largo, colores, estilo ideal" />
          </label>

          <label>
            <span>Observaciones adicionales</span>
            <textarea name="observaciones" value={form.observaciones} onChange={handleChange} rows="4" placeholder="Cualquier detalle importante" />
          </label>

          <button className="btn btn-primary" type="submit" disabled={loading}>
            {loading ? 'Guardando...' : 'Guardar ficha'}
          </button>
        </form>

        {savedEntries.length > 0 && (
          <div className="ficha-list-wrap">
            <h3>Mis fichas enviadas</h3>
            <ul className="ficha-list">
              {savedEntries.map((item) => (
                <li key={item.id}>
                  <strong>{item.servicio}</strong>
                  <span>{new Date(item.created_at).toLocaleString()}</span>
                  <small>{item.nombre} · {item.telefono}</small>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
    </section>
  )
}
