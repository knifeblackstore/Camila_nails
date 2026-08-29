// Protege páginas que requieren una sesión o permisos de administrador.
import { useContext } from 'react'
import { Navigate } from 'react-router-dom'
import { AuthContext } from '../AuthProvider'

export default function ProtectedRoute({ children, adminOnly }) {
  const { user, authReady } = useContext(AuthContext)
  if (!authReady) return null
  // Redirige a login cuando no existe una sesión activa.
  if (!user) return <Navigate to="/login" replace />
  // Redirige al inicio a los usuarios sin permisos administrativos.
  if (adminOnly && user.role !== 'admin' && user.email !== 'admin@admin.com') {
    return <Navigate to="/" replace />
  }
  return children
}
