// Modal reutilizable para mostrar una enfermedad y su imagen ampliada.
import React from 'react'

export default function Lightbox({ item, onClose }) {
  // Si no hay elemento seleccionado, el modal permanece oculto.
  if (!item) return null

  return (
    <div className="lightbox" role="dialog" aria-modal="true" onClick={onClose}>
      <div className="lightbox-content" onClick={(e) => e.stopPropagation()}>
        <button className="lightbox-close" onClick={onClose} aria-label="Cerrar">×</button>
        <div className="lightbox-media">
          <img src={item.img} alt={item.name} />
        </div>
        <div className="lightbox-info">
          <h3>{item.name}</h3>
          <p>{item.desc}</p>
        </div>
      </div>
    </div>
  )
}
