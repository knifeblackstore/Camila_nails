// Barra de navegación principal y controles de sesión del usuario.
import React, { useContext } from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { AuthContext } from '../AuthProvider'
import logo from '../assets/logo-camila-nails.png.jpeg'

export default function Navbar() {
  const { user, logout } = useContext(AuthContext)
  const nav = useNavigate()

  // Cierra la sesión y devuelve al usuario a la página principal.
  function handleLogout() {
    logout()
    nav('/')
  }

  const isAdmin = user?.role === 'admin' || user?.email === 'admin@admin.com'
  const canSeeFicha = Boolean(user)

  return (
    <header className="nav">
      <div className="nav-inner">
        <Link to="/" className="brand"><img src={logo} alt="Camila nails" /><span>Camila nails</span></Link>
        <nav className="links">
          <Link to="/about">Historia</Link>
          <Link to="/styles">Estilos</Link>
          <Link to="/polishes">Esmaltes</Link>
          <Link to="/diseases">Enfermedades</Link>
          <Link to="/contact">Agendar</Link>
          {canSeeFicha && <Link to="/ficha-tecnica">Ficha técnica</Link>}
        </nav>
        <div className="actions">
          {user ? (
            <>
              <span className="user">{user.username || user.email}</span>
              <Link to="/profile" className="profile-link">Mi perfil</Link>
              {isAdmin && <Link to="/admin" className="admin-link">Panel de administración</Link>}
              <button onClick={handleLogout} className="btn-ghost">Salir</button>
            </>
          ) : (
            <>
              <Link to="/login">Iniciar sesión</Link>
              <Link to="/register" className="pill">Registro</Link>
            </>
          )}
        </div>
      </div>
    </header>
  )
}
