// Pantalla para crear una cuenta de cliente.
import React, { useContext, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { AuthContext } from '../AuthProvider'
import logo from '../assets/logo-camila-nails.png.jpeg'

export default function Register() {
  const { register } = useContext(AuthContext)
  const [name, setName] = useState('')
  const [username, setUsername] = useState('')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [msg, setMsg] = useState(null) // Mostrar resultado del registro
  const nav = useNavigate()

  // Registra la cuenta y redirige al inicio después de mostrar el resultado.
  // Enviar formulario de registro y esperar la promesa
  async function submit(e) {
    e.preventDefault()
    const res = await register({ name, username, email, password })
    if (res && res.success) {
      setMsg({ type: 'success', text: res.message || 'Registro exitoso' })
      setTimeout(() => nav('/'), 900)
    } else {
      setMsg({ type: 'error', text: res?.error || 'Error en el registro' })
    }
  }

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-brand"><img src={logo} alt="Camila nails" /><span>Camila nails</span></div>
        <h2>Registro</h2>
        <form onSubmit={submit} className="auth-form" aria-label="register-form">
          <div className="field">
            <input placeholder=" " value={name} onChange={(e) => setName(e.target.value)} required />
            <label>Nombre</label>
          </div>

          <div className="field">
            <input placeholder=" " value={username} onChange={(e) => setUsername(e.target.value)} required />
            <label>Usuario</label>
          </div>

          <div className="field">
            <input placeholder=" " value={email} onChange={(e) => setEmail(e.target.value)} required />
            <label>Email</label>
          </div>

          <div className="field">
            <input type="password" placeholder=" " value={password} onChange={(e) => setPassword(e.target.value)} required />
            <label>Contraseña</label>
          </div>

          <div className="auth-actions">
            <button className="btn" type="submit">Crear cuenta</button>
            <div>
              <small>¿Ya tienes cuenta? <a href="/login">Entrar</a></small>
            </div>
          </div>
        </form>

        {msg && (
          <div className={msg.type === 'success' ? 'notice success' : 'notice error'}>
            {msg.text}
          </div>
        )}
      </div>
    </div>
  )
}
