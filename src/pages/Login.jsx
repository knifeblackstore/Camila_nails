// Pantalla de autenticación para clientes y administradores.
import React, { useContext, useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { AuthContext } from '../AuthProvider'
import logo from '../assets/logo-camila-nails.png.jpeg'

export default function Login() {
  const { login } = useContext(AuthContext)
  const [username, setUsername] = useState('')
  const [password, setPassword] = useState('')
  const [msg, setMsg] = useState(null) // Mensaje de éxito o error
  const nav = useNavigate()

  // Valida las credenciales y vuelve al inicio cuando el acceso es correcto.
  // submit: usa login({ username, password }) que es async
  async function submit(e) {
    e.preventDefault()
    const res = await login({ username, password })
    if (res && res.success) {
      setMsg({ type: 'success', text: res.message || 'Autenticación correcta' })
      setTimeout(() => nav('/'), 700)
    } else {
      setMsg({ type: 'error', text: res?.error || 'Error en la autenticación' })
    }
  }

  return (
    <div className="auth-page">
      <div className="auth-card">
        <div className="auth-brand"><img src={logo} alt="Camila nails" /><span>Camila nails</span></div>
        <h2>Iniciar sesión</h2>
        <form onSubmit={submit} className="auth-form" aria-label="login-form">
          {/* Campo para username o email con etiqueta animada */}
          <div className="field">
            <input
              placeholder=" "
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              aria-label="usuario o email"
            />
            <label>Usuario o email</label>
          </div>

          {/* Campo contraseña */}
          <div className="field">
            <input
              type="password"
              placeholder=" "
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              aria-label="contraseña"
            />
            <label>Contraseña</label>
          </div>

          <div className="auth-actions">
            <button className="btn" type="submit">Entrar</button>
            <div>
              <small>¿No tienes cuenta? <a href="/register">Regístrate</a></small>
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
