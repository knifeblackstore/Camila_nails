// Perfil protegido donde cada usuario puede actualizar su nombre visible.
import React, { useContext, useState } from 'react'
import { AuthContext } from '../AuthProvider'

export default function Profile() {
  const { user, updateProfile } = useContext(AuthContext)
  const [name, setName] = useState(user?.name || '')
  const [message, setMessage] = useState(null)
  const [saving, setSaving] = useState(false)

  // Guarda el nombre y conserva la información de sesión existente.
  async function submit(event) {
    event.preventDefault()
    setSaving(true)
    setMessage(null)
    const result = await updateProfile({ name })
    setSaving(false)
    setMessage({ type: result.success ? 'success' : 'error', text: result.message || result.error })
  }

  return (
    <section className="page profile-page">
      <div className="profile-card">
        <p className="eyebrow">Cuenta personal</p>
        <h2>Mi perfil</h2>
        <p className="profile-intro">Actualiza el nombre que aparece en tu cuenta de Camila nails.</p>
        <form className="form profile-form" onSubmit={submit}>
          <label>
            Nombre
            <input value={name} onChange={(event) => setName(event.target.value)} required maxLength={80} />
          </label>
          <label>
            Usuario
            <input value={user?.username || ''} readOnly />
          </label>
          <button className="btn" type="submit" disabled={saving}>
            {saving ? 'Guardando...' : 'Guardar cambios'}
          </button>
        </form>
        {message && <div className={message.type === 'success' ? 'notice success' : 'notice error'}>{message.text}</div>}
      </div>
    </section>
  )
}
