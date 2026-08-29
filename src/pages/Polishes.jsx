// Catálogo informativo de marcas de esmaltes agrupadas por tipo de uso.
import React, { useContext } from 'react'
import { AuthContext } from '../AuthProvider'

const brandGroups = [
  {
    title: 'Marcas populares y de uso local',
    brands: [
      { name: 'Masglo', description: 'Marca tradicional muy popular en Colombia, reconocida por su duración, sistema de pincel plano y esmaltes semipermanentes.' },
      { name: 'Vogue', description: 'Marca de alta disponibilidad en tiendas y farmacias locales, famosa por su línea de efecto gel y secado rápido.' },
      { name: 'Rimmel London', description: 'Ofrece opciones accesibles como la línea Super Gel.' },
      { name: 'Maybelline', description: 'Cuenta con esmaltes de secado rápido y gran variedad comercial.' },
    ],
  },
  {
    title: 'Marcas de gel semipermanente y caseras',
    brands: [
      { name: 'Beetles', description: 'Muy buscado en kits para principiantes y uso en casa con lámpara UV.' },
      { name: 'Semilac', description: 'Referente europeo en esmaltes permanentes de alta pigmentación.' },
      { name: 'Bluesky', description: 'Alternativa económica muy usada para manicura en gel.' },
      { name: 'Claresa', description: 'Alternativa económica muy usada para manicura en gel.' },
    ],
  },
]

export default function Polishes() {
  const { user } = useContext(AuthContext)
  const isAdmin = user?.role === 'admin' || user?.email === 'admin@admin.com'

  // Permite que el administrador actualice la descripción de una marca.
  function propose(brand) {
    if (!user) return alert('Inicia sesión para proponer cambios')
    const t = window.prompt('Editar descripción de ' + brand.name, brand.description)
    if (t) {
      fetch('/api/pending', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ page: `polishes.${brand.name}`, content: t, author: user.email || user.username }),
      })
        .then((r) => r.json())
        .then((d) => {
          if (d && d.success) alert('Enviado para autorización')
          else alert('Error: ' + (d.error || ''))
        })
        .catch(() => {
          const pending = JSON.parse(localStorage.getItem('kb_pending') || '[]')
          pending.push({ id: Date.now(), page: `polishes.${brand.name}`, content: t, author: user.email || user.username, date: new Date().toISOString() })
          localStorage.setItem('kb_pending', JSON.stringify(pending))
          alert('Guardado localmente (offline)')
        })
    }
  }

  return (
    <section className="page polishes">
      <h2>Esmaltes</h2>
      <p className="polishes-intro">Conoce algunas marcas populares para encontrar el acabado ideal para tus uñas.</p>
      <div className="polish-groups">
        {brandGroups.map((group) => (
          <section className="polish-group" key={group.title}>
            <h3>{group.title}</h3>
            <div className="polish-list">
              {group.brands.map((brand) => (
                <article key={brand.name} className="polish">
                  <strong>{brand.name}</strong>
                  <p>{brand.description}</p>
                  {isAdmin && <button className="btn tiny" onClick={() => propose(brand)}>Editar</button>}
                </article>
              ))}
            </div>
          </section>
        ))}
      </div>
    </section>
  )
}
