// Formulario de reserva que prepara los datos para enviarlos por WhatsApp.
import React, { useState } from 'react'

export default function Contact() {
  // Conserva los valores escritos en el formulario de cita.
  const [form, setForm] = useState({ name: '', phone: '', date: '', time: '', notes: '' })

  const MANICURIST_PHONE = '573102864177' // Número provisto por el usuario sin + ni 00

    // Actualiza únicamente el campo que cambió.
  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value })
  }

  function submit(e) {
    e.preventDefault()
    const text = `Reserva%20de%20cita%0ACliente:%20${encodeURIComponent(form.name)}%0ATeléfono:%20${encodeURIComponent(form.phone)}%0AFecha:%20${encodeURIComponent(form.date)}%0AHora:%20${encodeURIComponent(form.time)}%0ANotas:%20${encodeURIComponent(form.notes)}`
    const url = `https://wa.me/${MANICURIST_PHONE}?text=${text}`
    window.open(url, '_blank')
  }

  return (
    <section id="contact" className="page contact">
      <h2>Agendar cita por WhatsApp</h2>
      <form onSubmit={submit} className="form">
        <label>
          Nombre
          <input name="name" value={form.name} onChange={handleChange} required />
        </label>
        <label>
          Teléfono
          <input name="phone" value={form.phone} onChange={handleChange} required />
        </label>
        <label>
          Fecha
          <input type="date" name="date" value={form.date} onChange={handleChange} required />
        </label>
        <label>
          Hora
          <input type="time" name="time" value={form.time} onChange={handleChange} required />
        </label>
        <label>
          Notas
          <textarea name="notes" value={form.notes} onChange={handleChange} />
        </label>
        <button className="btn" type="submit">Ir a WhatsApp</button>
      </form>
    </section>
  )
}
