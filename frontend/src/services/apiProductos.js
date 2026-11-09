const API_BASE = 'http://127.0.0.1:8000/api';

export async function listarProductos() {
  const response = await fetch(`${API_BASE}/productos/`);
  if (!response.ok) throw new Error('No se pudo cargar el catálogo');
  return response.json();
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
