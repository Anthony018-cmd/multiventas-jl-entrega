import { useEffect, useState } from 'react';
import { listarProductos } from '../services/apiProductos';

export default function Catalogo() {
  const [productos, setProductos] = useState([]);
  const [estado, setEstado] = useState('Cargando productos...');
  useEffect(() => { listarProductos().then((data) => { setProductos(data); setEstado(''); }).catch((error) => setEstado(error.message)); }, []);
  return <section className="catalogo"><div className="section-heading"><p className="eyebrow">Catálogo Multiventas JL</p><h2>Accesorios para tu equipo</h2><p>Compra desde casa y elige recojo en tienda o envío por Shalom.</p></div>{estado && <p className="feedback">{estado}</p>}<div className="product-grid">{productos.map((producto) => <article className="product-card" key={producto.id}><div className="product-image">{producto.imagen ? <img src={producto.imagen} alt={producto.nombre} /> : <span>Multiventas JL</span>}</div><p className="product-category">{producto.categoria}</p><h3>{producto.nombre}</h3><p className="product-price">S/ {Number(producto.precio).toFixed(2)}</p><p className="stock">{producto.stock} unidades disponibles</p><a className="button secondary" href={`/producto/${producto.id}`}>Ver ficha</a></article>)}</div></section>;
}
