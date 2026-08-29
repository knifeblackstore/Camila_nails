import { createContext, useState } from 'react'

export const AuthContext = createContext(null)

export function AuthProvider({ children }) {
  // Estado del usuario autenticado (sin contraseña)
  const [user, setUser] = useState(() => {
    const stored = localStorage.getItem('kb_user')
    if (!stored) return null
    try {
      const parsed = JSON.parse(stored)
      return parsed
    } catch {
      localStorage.removeItem('kb_user')
      return null
    }
  })

  function saveSession(nextUser) {
    const session = { ...nextUser }
    setUser(session)
    localStorage.setItem('kb_user', JSON.stringify(session))
  }

  // Helper: hash SHA-256 para contraseñas (cliente). Devuelve hex string.
  async function hashPassword(password) {
    const enc = new TextEncoder()
    const data = enc.encode(password)
    const hashBuffer = await crypto.subtle.digest('SHA-256', data)
    const hashArray = Array.from(new Uint8Array(hashBuffer))
    return hashArray.map((b) => b.toString(16).padStart(2, '0')).join('')
  }

  /**
   * register({ name, username, email, password })
   * - Registra usuario en `kb_users` con password hash.
   * - Devuelve { success, message/error } y hace login automático.
   */
  async function register({ name, username, email, password }) {
    if (!username || !password || !email) {
      return { success: false, error: 'Faltan campos obligatorios' }
    }
    // Try server-side registration first
    try {
      const resp = await fetch('/api/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name, username, email, password }),
      })
      const data = await resp.json()
      if (!resp.ok) return { success: false, error: data.error || 'Error en el registro' }
      // After successful server register, perform local login (get user from server)
      const safeUser = { name, username, email, role: 'user' }
      saveSession(safeUser)
      return { success: true, message: data.message || 'Registro exitoso' }
    } catch (err) {
      // Fallback to localStorage-based registration (offline)
      console.warn('server register failed, falling back to local', err)
      const users = JSON.parse(localStorage.getItem('kb_users') || '[]')
      if (users.find((u) => u.username === username)) {
        return { success: false, error: 'El nombre de usuario ya existe' }
      }
      if (users.find((u) => u.email === email)) {
        return { success: false, error: 'El email ya está registrado' }
      }
      const pwdHash = await hashPassword(password)
      const newUser = { name: name || '', username, email, passwordHash: pwdHash }
      users.push(newUser)
      localStorage.setItem('kb_users', JSON.stringify(users))
      const safeUser = { name: newUser.name, username: newUser.username, email: newUser.email, role: 'user' }
      saveSession(safeUser)
      return { success: true, message: 'Registro local exitoso (offline mode)' }
    }
  }

  /**
   * login({ username, password })
   * - Busca por `username` (o email) y compara hash.
   */
  async function login({ username, password }) {
    if (!username || !password) return { success: false, error: 'Usuario y contraseña requeridos' }
    try {
      const resp = await fetch('/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username, password }),
      })
      const data = await resp.json()
      if (!resp.ok) return { success: false, error: data.error || 'Error en la autenticación' }
      const u = data.user
      saveSession(u)
      return { success: true, message: data.message || 'Autenticación exitosa', user: u }
    } catch (err) {
      // Fallback to localStorage auth
      console.warn('server login failed, falling back to local', err)
      const users = JSON.parse(localStorage.getItem('kb_users') || '[]')
      const userRecord = users.find((u) => u.username === username || u.email === username)
      if (!userRecord) return { success: false, error: 'Usuario no encontrado (offline)' }
      const pwdHash = await hashPassword(password)
      if (pwdHash !== userRecord.passwordHash) return { success: false, error: 'Contraseña incorrecta (offline)' }
      const safeUser = { name: userRecord.name, username: userRecord.username, email: userRecord.email, role: userRecord.role || 'user' }
      saveSession(safeUser)
      return { success: true, message: 'Autenticación local exitosa', user: safeUser }
    }
  }

  function logout() {
    setUser(null)
    localStorage.removeItem('kb_user')
  }

  // Actualiza el nombre visible en el servidor o conserva el cambio localmente.
  async function updateProfile({ name }) {
    const cleanName = name.trim()
    if (!cleanName) return { success: false, error: 'El nombre es obligatorio' }
    try {
      const resp = await fetch('/api/profile', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ id: user.id, email: user.email, name: cleanName }),
      })
      const data = await resp.json()
      if (!resp.ok) return { success: false, error: data.error || 'No se pudo actualizar el perfil' }
      saveSession(data.user)
      return { success: true, message: 'Nombre actualizado correctamente' }
    } catch {
      // Permite seguir usando el perfil aunque el backend esté desconectado.
      const updatedUser = { ...user, name: cleanName }
      saveSession(updatedUser)
      return { success: true, message: 'Nombre actualizado localmente' }
    }
  }

  return (
    <AuthContext.Provider value={{ user, authReady: true, login, logout, register, updateProfile }}>
      {children}
    </AuthContext.Provider>
  )
}

export default AuthProvider
