import { useEffect, useState } from 'react';
import { crearPedido } from '../services/apiProductos';

export default function Carrito() {
  const [carrito, setCarrito] = useState([]); const [metodo, setMetodo] = useState('RECOJO'); const [mensaje, setMensaje] = useState('');
  useEffect(() => setCarrito(JSON.parse(localStorage.getItem('multiventas-carrito') || '[]')), []);
  function guardar(items) { setCarrito(items); localStorage.setItem('multiventas-carrito', JSON.stringify(items)); }
  async function confirmarPedido() { try { const pedido = await crearPedido(metodo, carrito.map((item) => ({ producto_id: item.id, cantidad: item.cantidad }))); guardar([]); setMensaje(`Pedido #${pedido.id} creado. Total: S/ ${Number(pedido.total).toFixed(2)}.`); } catch (error) { setMensaje(error.message); } }
  const total = carrito.reduce((sum, item) => sum + Number(item.precio) * item.cantidad, 0);
  return <section className="cart-card"><p className="eyebrow">Compra</p><h1>Tu carrito</h1>{carrito.length === 0 ? <p className="feedback">Tu carrito está vacío. <a href="/">Ver catálogo</a></p> : <><div className="cart-lines">{carrito.map((item) => <div className="cart-line" key={item.id}><div><strong>{item.nombre}</strong><span>S/ {Number(item.precio).toFixed(2)} × {item.cantidad}</span></div><button type="button" onClick={() => guardar(carrito.filter((line) => line.id !== item.id))}>Quitar</button></div>)}</div><p className="cart-total">Total: S/ {total.toFixed(2)}</p><label className="delivery">Entrega<select value={metodo} onChange={(event) => setMetodo(event.target.value)}><option value="RECOJO">Recojo en tienda</option><option value="ENVIO_SHALOM">Envío por Shalom</option></select></label><button className="button" type="button" onClick={confirmarPedido}>Confirmar pedido</button></>}{mensaje && <p className="feedback">{mensaje}</p>}</section>;
}
