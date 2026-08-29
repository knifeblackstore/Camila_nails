// Componente raíz: conecta autenticación, navegación y todas las páginas.
import './App.css'
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import { AuthProvider } from './AuthProvider'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import About from './pages/About'
import Styles from './pages/Styles'
import Polishes from './pages/Polishes'
import Diseases from './pages/Diseases'
import Contact from './pages/Contact'
import Login from './pages/Login'
import Register from './pages/Register'
import Profile from './pages/Profile'
import AdminPanel from './pages/AdminPanel'
import FichaTecnica from './pages/FichaTecnica'
import ProtectedRoute from './components/ProtectedRoute'

function App() {
    // El proveedor mantiene la sesión disponible para toda la aplicación.
  return (
    <AuthProvider>
      <BrowserRouter>
        <Navbar />
        <main className="app-container">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/styles" element={<Styles />} />
            <Route path="/polishes" element={<Polishes />} />
            <Route path="/diseases" element={<Diseases />} />
            <Route
              path="/contact"
              element={
                <ProtectedRoute>
                  <Contact />
                </ProtectedRoute>
              }
            />
            <Route path="/login" element={<Login />} />
            <Route path="/register" element={<Register />} />
            <Route
              path="/profile"
              element={
                <ProtectedRoute>
                  <Profile />
                </ProtectedRoute>
              }
            />
            <Route
              path="/ficha-tecnica"
              element={
                <ProtectedRoute>
                  <FichaTecnica />
                </ProtectedRoute>
              }
            />
            <Route
              path="/admin"
              element={
                <ProtectedRoute adminOnly>
                  <AdminPanel />
                </ProtectedRoute>
              }
            />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </main>
      </BrowserRouter>
    </AuthProvider>
  )
}

export default App