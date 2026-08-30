require('dotenv').config()

const express = require('express')
const cors = require('cors')
const path = require('path')
const fs = require('fs')
const multer = require('multer')
const bcrypt = require('bcryptjs')
const mysql = require('mysql2/promise')

const PORT = process.env.PORT || 4000
const app = express()
const DEFAULT_ADMIN = {
  username: 'camila_nails',
  email: 'admin@admin.com',
  password: '123456',
  role: 'admin',
}

app.use(cors())
app.use(express.json())

const pool = mysql.createPool({
  host: process.env.DB_HOST || 'localhost',
  port: Number(process.env.DB_PORT) || 3306,
  user: process.env.DB_USER || 'root',
  password: process.env.DB_PASSWORD || '',
  database: process.env.DB_NAME || 'camila_nails',
  waitForConnections: true,
  connectionLimit: 10,
  queueLimit: 0,
})

const uploadsDir = path.join(__dirname, 'uploads')
if (!fs.existsSync(uploadsDir)) fs.mkdirSync(uploadsDir, { recursive: true })

const storage = multer.diskStorage({
  destination: function (req, file, cb) { cb(null, uploadsDir) },
  filename: function (req, file, cb) {
    const unique = Date.now() + '-' + Math.round(Math.random() * 1e9)
    const name = unique + path.extname(file.originalname)
    cb(null, name)
  }
})
const upload = multer({ storage })

async function initDB() {
  const connection = await pool.getConnection()
  try {
    await connection.query(`
      CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) DEFAULT '',
        username VARCHAR(100) NOT NULL UNIQUE,
        email VARCHAR(255) NOT NULL UNIQUE,
        passwordHash VARCHAR(255) NOT NULL,
        role VARCHAR(50) DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `)

    await connection.query(`
      CREATE TABLE IF NOT EXISTS uploads (
        id INT AUTO_INCREMENT PRIMARY KEY,
        filename VARCHAR(255) NOT NULL,
        url VARCHAR(255) NOT NULL,
        style VARCHAR(255) DEFAULT '',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `)

    await connection.query(`
      CREATE TABLE IF NOT EXISTS pending (
        id INT AUTO_INCREMENT PRIMARY KEY,
        page VARCHAR(255),
        content TEXT,
        author VARCHAR(255),
        date DATETIME,
        approved TINYINT DEFAULT 0
      )
    `)

    await connection.query('UPDATE pending SET approved = 1 WHERE approved = 0')

    await connection.query(`
      CREATE TABLE IF NOT EXISTS fichas (
        id INT AUTO_INCREMENT PRIMARY KEY,
        userId INT,
        username VARCHAR(255),
        email VARCHAR(255),
        nombre VARCHAR(255),
        telefono VARCHAR(255),
        servicio VARCHAR(255),
        estado_actual VARCHAR(255),
        alergias TEXT,
        enfermedades TEXT,
        historial TEXT,
        preferencia TEXT,
        observaciones TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      )
    `)

    const [existingAdmin] = await connection.query(
      'SELECT id FROM users WHERE username = ? OR email = ?',
      [DEFAULT_ADMIN.username, DEFAULT_ADMIN.email]
    )

    if (!existingAdmin.length) {
      const hash = await bcrypt.hash(DEFAULT_ADMIN.password, 10)
      await connection.query(
        'INSERT INTO users (name, username, email, role, passwordHash) VALUES (?, ?, ?, ?, ?)',
        [
          'Administrador',
          DEFAULT_ADMIN.username,
          DEFAULT_ADMIN.email,
          DEFAULT_ADMIN.role,
          hash,
        ]
      )
    }
  } finally {
    connection.release()
  }
}

app.use('/uploads', express.static(uploadsDir))

app.post('/api/register', async (req, res) => {
  const { name, username, email, password } = req.body
  if (!username || !email || !password) {
    return res.status(400).json({ success: false, error: 'Faltan campos' })
  }

  try {
    const hash = await bcrypt.hash(password, 10)
    const [existing] = await pool.query(
      'SELECT id FROM users WHERE username = ? OR email = ?',
      [username, email]
    )

    if (existing.length > 0) {
      return res.status(409).json({ success: false, error: 'Usuario o email ya existe' })
    }

    await pool.query(
      'INSERT INTO users (name, username, email, passwordHash, role) VALUES (?, ?, ?, ?, ?)',
      [name || '', username, email, hash, 'user']
    )

    return res.json({ success: true, message: 'Registro exitoso' })
  } catch (err) {
    console.error(err)
    return res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.post('/api/login', async (req, res) => {
  const { username, password } = req.body
  if (!username || !password) {
    return res.status(400).json({ success: false, error: 'Faltan campos' })
  }

  try {
    const [rows] = await pool.query(
      'SELECT * FROM users WHERE username = ? OR email = ?',
      [username, username]
    )

    const user = rows[0]
    if (!user) {
      return res.status(404).json({ success: false, error: 'Usuario no encontrado' })
    }

    const match = await bcrypt.compare(password, user.passwordHash)
    if (!match) {
      return res.status(401).json({ success: false, error: 'Contraseña incorrecta' })
    }

    const role = user.role || (user.email === 'admin@admin.com' ? 'admin' : 'user')
    const safe = { id: user.id, name: user.name, username: user.username, email: user.email, role }

    return res.json({ success: true, message: 'Autenticación exitosa', user: safe })
  } catch (err) {
    console.error(err)
    return res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.put('/api/profile', async (req, res) => {
  const { id, email, name } = req.body
  const cleanName = typeof name === 'string' ? name.trim() : ''

  if (!cleanName) {
    return res.status(400).json({ success: false, error: 'El nombre es obligatorio' })
  }

  try {
    const [rows] = await pool.query(
      'SELECT * FROM users WHERE id = ? OR email = ?',
      [id, email]
    )

    const user = rows[0]
    if (!user) {
      return res.status(404).json({ success: false, error: 'Usuario no encontrado' })
    }

    await pool.query('UPDATE users SET name = ? WHERE id = ?', [cleanName, user.id])

    const safe = {
      id: user.id,
      name: cleanName,
      username: user.username,
      email: user.email,
      role: user.role || (user.email === 'admin@admin.com' ? 'admin' : 'user')
    }

    return res.json({ success: true, user: safe })
  } catch (err) {
    console.error(err)
    return res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.post('/api/upload', upload.single('file'), async (req, res) => {
  if (!req.file) {
    return res.status(400).json({ success: false, error: 'No file' })
  }

  const url = `/uploads/${req.file.filename}`

  try {
    await pool.query(
      'INSERT INTO uploads (filename, url, style) VALUES (?, ?, ?)',
      [req.file.filename, url, req.body.style || '']
    )

    return res.json({ success: true, url })
  } catch (err) {
    console.error(err)
    return res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.get('/api/uploads', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM uploads ORDER BY id DESC')
    res.json(rows)
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.get('/api/fichas', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM fichas ORDER BY id DESC')
    res.json(rows)
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.post('/api/fichas', async (req, res) => {
  const { userId, username, email, nombre, telefono, servicio, estado_actual, alergias, enfermedades, historial, preferencia, observaciones } = req.body

  if (!nombre || !telefono || !servicio) {
    return res.status(400).json({ success: false, error: 'Faltan datos obligatorios' })
  }

  try {
    const [result] = await pool.query(
      `INSERT INTO fichas
       (userId, username, email, nombre, telefono, servicio, estado_actual, alergias, enfermedades, historial, preferencia, observaciones)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`,
      [userId || null, username || '', email || '', nombre, telefono, servicio, estado_actual || 'Normal', alergias || '', enfermedades || '', historial || '', preferencia || '', observaciones || '']
    )

    res.json({ success: true, id: result.insertId })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.put('/api/fichas/:id', async (req, res) => {
  const id = Number(req.params.id)
  const { nombre, telefono, servicio, estado_actual, alergias, enfermedades, historial, preferencia, observaciones } = req.body

  if (!id || !nombre || !telefono || !servicio) {
    return res.status(400).json({ success: false, error: 'Faltan campos obligatorios' })
  }

  try {
    await pool.query(
      `UPDATE fichas SET 
        nombre = ?, telefono = ?, servicio = ?, estado_actual = ?, 
        alergias = ?, enfermedades = ?, historial = ?, preferencia = ?, observaciones = ? 
       WHERE id = ?`,
      [nombre, telefono, servicio, estado_actual || 'Normal', alergias || '', enfermedades || '', historial || '', preferencia || '', observaciones || '', id]
    )
    res.json({ success: true, message: 'Ficha actualizada' })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.delete('/api/fichas/:id', async (req, res) => {
  const id = Number(req.params.id)
  if (!id) return res.status(400).json({ success: false, error: 'ID inválido' })
  
  try {
    await pool.query('DELETE FROM fichas WHERE id = ?', [id])
    res.json({ success: true, message: 'Ficha eliminada' })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.get('/api/users', async (req, res) => {
  try {
    const [rows] = await pool.query(
      'SELECT id, name, username, email, role FROM users ORDER BY id ASC'
    )
    res.json(rows)
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.post('/api/users', async (req, res) => {
  const { name, username, email, password, role = 'user' } = req.body
  if (!username || !email || !password) {
    return res.status(400).json({ success: false, error: 'Faltan campos obligatorios' })
  }

  try {
    const hash = await bcrypt.hash(password, 10)
    const [existing] = await pool.query(
      'SELECT id FROM users WHERE username = ? OR email = ?',
      [username, email]
    )

    if (existing.length > 0) {
      return res.status(409).json({ success: false, error: 'Usuario o email ya existe' })
    }

    const [result] = await pool.query(
      'INSERT INTO users (name, username, email, passwordHash, role) VALUES (?, ?, ?, ?, ?)',
      [name || '', username, email, hash, role === 'admin' ? 'admin' : 'user']
    )

    res.json({ success: true, id: result.insertId, message: 'Usuario creado correctamente' })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.patch('/api/users/:id/role', async (req, res) => {
  const id = Number(req.params.id)
  const { role } = req.body

  if (!id || !role || !['admin', 'user'].includes(role)) {
    return res.status(400).json({ success: false, error: 'Rol inválido' })
  }

  try {
    await pool.query('UPDATE users SET role = ? WHERE id = ?', [role, id])
    res.json({ success: true, message: 'Rol actualizado' })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.put('/api/users/:id', async (req, res) => {
  const id = Number(req.params.id)
  const { name, username, email } = req.body

  if (!id || !username || !email) {
    return res.status(400).json({ success: false, error: 'Faltan campos obligatorios' })
  }

  try {
    const [existing] = await pool.query(
      'SELECT id FROM users WHERE (username = ? OR email = ?) AND id != ?',
      [username, email, id]
    )

    if (existing.length > 0) {
      return res.status(409).json({ success: false, error: 'El usuario o email ya está en uso por otra persona' })
    }

    await pool.query(
      'UPDATE users SET name = ?, username = ?, email = ? WHERE id = ?',
      [name || '', username, email, id]
    )
    res.json({ success: true, message: 'Usuario actualizado correctamente' })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.delete('/api/users/:id', async (req, res) => {
  const id = Number(req.params.id)
  if (!id) return res.status(400).json({ success: false, error: 'ID inválido' })
  
  try {
    await pool.query('DELETE FROM users WHERE id = ?', [id])
    res.json({ success: true, message: 'Usuario eliminado' })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.post('/api/pending', async (req, res) => {
  const { page, content, author } = req.body
  const date = new Date().toISOString()

  try {
    const [result] = await pool.query(
      'INSERT INTO pending (page, content, author, date, approved) VALUES (?, ?, ?, ?, ?)',
      [page, content, author, date, 1]
    )

    res.json({ success: true, id: result.insertId, approved: true })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.get('/api/pending', async (req, res) => {
  try {
    const [rows] = await pool.query('SELECT * FROM pending WHERE approved = 0 ORDER BY id DESC')
    res.json(rows)
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.post('/api/pending/:id/approve', async (req, res) => {
  const id = Number(req.params.id)

  try {
    await pool.query('UPDATE pending SET approved = 1 WHERE id = ?', [id])
    res.json({ success: true })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

app.post('/api/pending/:id/reject', async (req, res) => {
  const id = Number(req.params.id)

  try {
    await pool.query('DELETE FROM pending WHERE id = ?', [id])
    res.json({ success: true })
  } catch (err) {
    console.error(err)
    res.status(500).json({ success: false, error: 'Error interno' })
  }
})

initDB()
  .then(() => {
    app.listen(PORT, () => console.log('Server running on', PORT))
  })
  .catch((err) => {
    console.error('MySQL connection error:', err)
    process.exit(1)
  })
