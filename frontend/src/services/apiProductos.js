const API_BASE = 'http://127.0.0.1:8000/api';

const PRODUCTOS_DEMO = [
  { id: 1, nombre: 'Audifonos Bluetooth', precio: 59.9, stock: 12, categoria: 'Audio' },
  { id: 2, nombre: 'Cargador rapido USB-C', precio: 39.9, stock: 20, categoria: 'Cargadores' },
  { id: 3, nombre: 'Cable USB-C reforzado', precio: 24.9, stock: 18, categoria: 'Accesorios' },
  { id: 4, nombre: 'Soporte para celular', precio: 29.9, stock: 10, categoria: 'Accesorios' },
  { id: 5, nombre: 'Power Bank 10000 mAh', precio: 79.9, stock: 8, categoria: 'Energia' },
  { id: 6, nombre: 'Funda para celular', precio: 19.9, stock: 25, categoria: 'Proteccion' },
];

export async function listarProductos() {
  try {
    const response = await fetch(`${API_BASE}/productos/`);
    if (!response.ok) throw new Error('API no disponible');
    return response.json();
  } catch {
    return PRODUCTOS_DEMO;
  }
}

export async function crearPedido(metodoEntrega, items) {
  const response = await fetch(`${API_BASE}/pedidos/`, {
    method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ metodo_entrega: metodoEntrega, items }),
  });
  const data = await response.json();
  if (!response.ok) throw new Error(data.error || 'No se pudo crear el pedido');
  return data;
}
