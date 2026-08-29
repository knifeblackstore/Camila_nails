// Herramientas privadas para aprobar propuestas y administrar imágenes.
import React, { useEffect, useState } from 'react'

export default function AdminPanel() {
  const [pending, setPending] = useState([])
  const [approved, setApproved] = useState([])
  const [users, setUsers] = useState([])
  const [fichas, setFichas] = useState([])
  const [uploads, setUploads] = useState([])
  const [uploadStyle, setUploadStyle] = useState('')
  const [newUser, setNewUser] = useState({ name: '', username: '', email: '', password: '', role: 'user' })

  async function load() {
    try {
      const res = await fetch('/api/pending')
      const data = await res.json()
      setPending((data || []).filter((p) => !p.approved))
      setApproved((data || []).filter((p) => p.approved))
    } catch (err) {
      const localPend = JSON.parse(localStorage.getItem('kb_pending') || '[]')
      const localAppr = JSON.parse(localStorage.getItem('kb_approved') || '[]')
      setPending(localPend)
      setApproved(localAppr)
    }
  }

  async function loadUploads() {
    try {
      const r = await fetch('/api/uploads')
      const d = await r.json()
      setUploads(d)
    } catch (err) {
      setUploads([])
    }
  }

  async function loadUsers() {
    try {
      const res = await fetch('/api/users')
      const data = await res.json()
      setUsers(Array.isArray(data) ? data : [])
    } catch (err) {
      setUsers([])
    }
  }

  async function loadFichas() {
    try {
      const res = await fetch('/api/fichas')
      const data = await res.json()
      setFichas(Array.isArray(data) ? data : [])
    } catch (err) {
      setFichas([])
    }
  }

  useEffect(() => {
    load()
    loadUploads()
    loadUsers()
    loadFichas()
  }, [])

  async function approve(id) {
    try {
      await fetch(`/api/pending/${id}/approve`, { method: 'POST' })
      await load()
    } catch (err) {
      const p = pending.find((x) => x.id === id)
      if (!p) return
      const nPending = pending.filter((x) => x.id !== id)
      const nApproved = [p, ...approved]
      localStorage.setItem('kb_pending', JSON.stringify(nPending))
      localStorage.setItem('kb_approved', JSON.stringify(nApproved))
      setPending(nPending)
      setApproved(nApproved)
    }
  }

  async function reject(id) {
    try {
      await fetch(`/api/pending/${id}/reject`, { method: 'POST' })
      await load()
    } catch (err) {
      const nPending = pending.filter((x) => x.id !== id)
      localStorage.setItem('kb_pending', JSON.stringify(nPending))
      setPending(nPending)
    }
  }

  async function handleFile(e) {
    const f = e.target.files?.[0]
    if (!f) return
    if (!uploadStyle) {
      alert('Selecciona primero el servicio de la imagen')
      e.target.value = ''
      return
    }
    const form = new FormData()
    form.append('file', f)
    form.append('style', uploadStyle)
    const r = await fetch('/api/upload', { method: 'POST', body: form })
    const d = await r.json()
    if (d && d.success) {
      alert('Subida completa: ' + d.url)
      loadUploads()
    } else alert('Error al subir')
  }

  async function createUser(e) {
    e.preventDefault()
    if (!newUser.username || !newUser.email || !newUser.password) {
      alert('Completa usuario, email y contraseña')
      return
    }
    try {
      const res = await fetch('/api/users', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(newUser),
      })
      const data = await res.json()
      if (!res.ok) {
        alert(data.error || 'No se pudo crear el usuario')
        return
      }
      setNewUser({ name: '', username: '', email: '', password: '', role: 'user' })
      await loadUsers()
      alert('Usuario creado correctamente')
    } catch (err) {
      alert('Error al crear el usuario')
    }
  }

  async function changeRole(userId, nextRole) {
    try {
      const res = await fetch(`/api/users/${userId}/role`, {
        method: 'PATCH',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ role: nextRole }),
      })
      const data = await res.json()
      if (!res.ok) {
        alert(data.error || 'No se pudo cambiar el rol')
        return
      }
      await loadUsers()
    } catch (err) {
      alert('Error al cambiar el rol')
    }
  }

  const [editingUser, setEditingUser] = useState(null)
  
  async function saveUserEdit(e) {
    e.preventDefault()
    if (!editingUser.username || !editingUser.email) {
      alert('Usuario y email son obligatorios')
      return
    }
    try {
      const res = await fetch(`/api/users/${editingUser.id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(editingUser),
      })
      const data = await res.json()
      if (!res.ok) {
        alert(data.error || 'No se pudo actualizar el usuario')
        return
      }
      setEditingUser(null)
      await loadUsers()
      alert('Usuario actualizado correctamente')
    } catch (err) {
      alert('Error al actualizar el usuario')
    }
  }

  return (
    <section className="page admin-shell">
      <div className="admin-panel-header">
        <p className="eyebrow">Administración</p>
        <h2>Panel de control</h2>
      </div>

      <div className="admin-columns">
        <div className="admin-section">
          <h3>Crear usuario</h3>
          <form onSubmit={createUser} className="admin-form">
            <input value={newUser.name} onChange={(e) => setNewUser({ ...newUser, name: e.target.value })} placeholder="Nombre completo" />
            <input value={newUser.username} onChange={(e) => setNewUser({ ...newUser, username: e.target.value })} placeholder="Usuario" />
            <input type="email" value={newUser.email} onChange={(e) => setNewUser({ ...newUser, email: e.target.value })} placeholder="Email" />
            <input type="password" value={newUser.password} onChange={(e) => setNewUser({ ...newUser, password: e.target.value })} placeholder="Contraseña" />
            <select value={newUser.role} onChange={(e) => setNewUser({ ...newUser, role: e.target.value })}>
              <option value="user">Cliente</option>
              <option value="admin">Administrador</option>
            </select>
            <button type="submit" className="btn">Crear usuario</button>
          </form>

          <h3 style={{ marginTop: '24px' }}>Usuarios registrados</h3>
          {users.length === 0 && <p style={{ opacity: 0.6 }}>Sin usuarios.</p>}
          <ul className="admin-list">
            {users.map((u) => (
              <li key={u.id} className="pending-item">
                {editingUser && editingUser.id === u.id ? (
                  <form onSubmit={saveUserEdit} style={{ display: 'flex', flexDirection: 'column', gap: '8px' }}>
                    <input value={editingUser.name || ''} onChange={(e) => setEditingUser({ ...editingUser, name: e.target.value })} placeholder="Nombre" />
                    <input value={editingUser.username || ''} onChange={(e) => setEditingUser({ ...editingUser, username: e.target.value })} placeholder="Usuario" />
                    <input type="email" value={editingUser.email || ''} onChange={(e) => setEditingUser({ ...editingUser, email: e.target.value })} placeholder="Email" />
                    <div style={{ display: 'flex', gap: '8px' }}>
                      <button type="submit" className="btn tiny">Guardar</button>
                      <button type="button" className="btn ghost tiny" onClick={() => setEditingUser(null)}>Cancelar</button>
                    </div>
                  </form>
                ) : (
                  <>
                    <strong>{u.username}</strong> {u.name && <span style={{fontSize: '12px', opacity: 0.8}}>({u.name})</span>}
                    <div className="pending-meta">{u.email}</div>
                    <div className="pending-meta">Rol: <span style={{ fontWeight: 600, color: u.role === 'admin' ? 'var(--accent)' : 'var(--text)' }}>{u.role}</span></div>
                    <div style={{ marginTop: '10px', display: 'flex', gap: '10px', alignItems: 'center' }}>
                      <select value={u.role} onChange={(e) => changeRole(u.id, e.target.value)} style={{ fontSize: '12px' }}>
                        <option value="user">Cliente</option>
                        <option value="admin">Administrador</option>
                      </select>
                      <button className="btn ghost tiny" onClick={() => setEditingUser(u)}>Editar</button>
                    </div>
                  </>
                )}
              </li>
            ))}
          </ul>
        </div>

        <div className="admin-section">
          <h3>Fichas de clientes</h3>
          {fichas.length === 0 && <p style={{ opacity: 0.6 }}>Sin fichas.</p>}
          <ul className="admin-list">
            {fichas.map((f) => (
              <li key={f.id} className="pending-item">
                <strong>{f.nombre || f.username || 'Sin nombre'}</strong>
                <div className="pending-meta">{f.servicio}</div>
                <div className="pending-meta">{f.email || f.username}</div>
                <div className="pending-meta">Tel: {f.telefono || 'N/A'}</div>
                <div className="pending-meta" style={{ marginTop: '8px' }}>{new Date(f.created_at).toLocaleString()}</div>
              </li>
            ))}
          </ul>

          <h3 style={{ marginTop: '24px' }}>Subir imágenes</h3>
          <div className="admin-upload-box">
            <select value={uploadStyle} onChange={(e) => setUploadStyle(e.target.value)} aria-label="Servicio de la imagen">
              <option value="">Selecciona el servicio</option>
              <option value="Builder gel">Builder gel</option>
              <option value="Nivelación base rubber">Nivelación base rubber</option>
              <option value="Soft gel">Soft gel</option>
              <option value="Esmaltado semipermanente">Esmaltado semipermanente</option>
              <option value="Esmaltado tradicional">Esmaltado tradicional</option>
              <option value="Semipermanente pies">Semipermanente pies</option>
            </select>
            <input type="file" accept="image/*" onChange={handleFile} />
          </div>
          
          {uploads.length > 0 && (
            <>
              <div style={{ fontSize: '12px', fontWeight: 600, margin: '12px 0 8px', color: 'var(--text-h)' }}>Galeria ({uploads.length})</div>
              <ul className="admin-list" style={{ maxHeight: '200px' }}>
                {uploads.map((u) => (
                  <li key={u.id} className="pending-item compact" style={{ padding: '10px 12px' }}>
                    <a href={u.url} target="_blank" rel="noreferrer" style={{ color: 'var(--accent)', textDecoration: 'none', fontSize: '12px', wordBreak: 'break-all' }}>
                      📷 {u.filename}
                    </a>
                  </li>
                ))}
              </ul>
            </>
          )}
        </div>
      </div>

      {(pending.length > 0 || approved.length > 0) && (
        <div className="admin-columns" style={{ marginTop: '20px' }}>
          {pending.length > 0 && (
            <div className="admin-section">
              <h3>Cambios pendientes</h3>
              <ul className="admin-list">
                {pending.map((p) => (
                  <li key={p.id} className="pending-item">
                    <strong>{p.page}</strong>
                    <p>{p.content}</p>
                    <div className="pending-meta">{p.author} - {new Date(p.date).toLocaleString()}</div>
                    <div className="pending-actions">
                      <button className="btn tiny" onClick={() => approve(p.id)}>Aprobar</button>
                      <button className="btn ghost tiny" onClick={() => reject(p.id)}>Rechazar</button>
                    </div>
                  </li>
                ))}
              </ul>
            </div>
          )}

          {approved.length > 0 && (
            <div className="admin-section">
              <h3>Aprobados</h3>
              <ul className="admin-list">
                {approved.map((p) => (
                  <li key={p.id} className="pending-item compact"><strong>{p.page}</strong> - {p.content}</li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </section>
  )
}
