// Guía visual de condiciones frecuentes de las uñas.
import React, { useState } from 'react'
import Lightbox from '../components/Lightbox'

// Lista de condiciones con descripciones y ruta de imagen.
// Coloca las imágenes en `src/assets/diseases/` con los nombres indicados abajo.
const diseases = [
  {
    id: 'onicomicosis',
    name: 'Onicomicosis (Hongos)',
    desc: 'Uña amarilla, gruesa y deformada; ocasionada por infecciones fúngicas.',
    img: '/src/assets/diseases/1-onicomicosis.jpg',
  },
  {
    id: 'onicolisis',
    name: 'Onicólisis distal',
    desc: 'Uña desprendida del lecho ungueal, con separación en el borde distal.',
    img: '/src/assets/diseases/2-onicolisis.jpg',
  },
  {
    id: 'paroniquia',
    name: 'Paroniquia aguda',
    desc: 'Inflamación alrededor de la uña, a menudo con pus e infección bacteriana.',
    img: '/src/assets/diseases/3-paroniquia.jpg',
  },
  {
    id: 'onicocriptosis',
    name: 'Onicocriptosis (uñero)',
    desc: 'Uña clavada en la piel con dolor y posible sangrado o infección local.',
    img: '/src/assets/diseases/4-onicocriptosis.jpg',
  },
  {
    id: 'lineas-de-beau',
    name: 'Líneas de Beau',
    desc: 'Surcos transversales en la uña que indican trauma o interrupción temporal en la matriz.',
    img: '/src/assets/diseases/5-lineas-beau.jpg',
  },
  {
    id: 'leuconiquia',
    name: 'Leuconiquia punteada',
    desc: 'Manchas blancas puntiformes en la uña; suele estar relacionada con pequeños traumas.',
    img: '/src/assets/diseases/6-leuconiquia.jpg',
  },
  {
    id: 'uña-fragil',
    name: 'Síndrome de la uña frágil',
    desc: 'Uñas finas y quebradizas que se fragmentan con facilidad.',
    img: '/src/assets/diseases/7-una-fragil.jpg',
  },
  {
    id: 'psoriasis-ungueal',
    name: 'Psoriasis ungueal (Hoyuelos)',
    desc: 'Hoyuelos y depresiones en la lámina ungueal; asociado a psoriasis en piel.',
    img: '/src/assets/diseases/8-psoriasis.jpg',
  },
  {
    id: 'hematoma-subungueal',
    name: 'Hematoma subungueal',
    desc: 'Acumulación de sangre bajo la uña por traumatismo; coloración oscura o rojiza.',
    img: '/src/assets/diseases/9-hematoma.jpg',
  },
  {
    id: 'uña-verde',
    name: 'Síndrome de la uña verde (Pseudomonas)',
    desc: 'Coloración verdosa por infección bacteriana (pseudomonas) en ambientes húmedos.',
    img: '/src/assets/diseases/10-una-verde.jpg',
  },
]

export default function Diseases() {
  // Guarda la enfermedad activa para mostrarla en el lightbox.
  const [selected, setSelected] = useState(null)

  // Abre y cierra el detalle ampliado de una condición.
  function open(d) { setSelected(d) }
  function close() { setSelected(null) }

  return (
    <section className="page diseases">
      <h2>Guía de enfermedades de las uñas</h2>
      <p>Imágenes y descripciones de condiciones frecuentes. Haz clic en una tarjeta para ver más detalles.</p>

      <div className="diseases-grid">
        {diseases.map((d) => (
          <article key={d.id} className="disease-card" role="button" tabIndex={0} onClick={() => open(d)} onKeyDown={(e) => { if (e.key === 'Enter') open(d) }}>
            <div className="disease-img-wrap">
              <img src={d.img} alt={d.name} onError={(e) => { e.currentTarget.style.display = 'none' }} />
              <div className="disease-placeholder">{d.name}</div>
            </div>

            <div className="disease-body">
              <h3>{d.name}</h3>
              <p>{d.desc}</p>
            </div>
          </article>
        ))}
      </div>

      {/* Lightbox modal */}
      <Lightbox item={selected} onClose={close} />

      <h3>Consejos generales</h3>
      <ul>
        <li>Mantén las uñas limpias y secas para evitar infecciones.</li>
        <li>No cortes ni empujes cutículas agresivamente; usa herramientas esterilizadas.</li>
        <li>Consulta a un profesional ante dolor, cambio de color o secreción.</li>
        <li>Evita permanecer con las manos húmedas por períodos prolongados.</li>
      </ul>
    </section>
  )
}
