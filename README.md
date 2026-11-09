# Multiventas JL

Prototipo IDL 2 de catálogo público, ficha de producto y carrito para Multiventas JL.

## Estructura

- `frontend/`: Astro + React. Inicio, catálogo, ficha y carrito.
- `backend/`: Django. API de productos y pedidos, con dominio DDD.
- `tienda/` y `multiventas_backend/`: avance administrativo del equipo.

## Ejecución local

Backend:

```powershell
cd backend
python manage.py runserver 0.0.0.0:8000
```

Frontend:

```powershell
cd frontend
npm.cmd install
npm.cmd run dev -- --host 127.0.0.1 --port 4321
```

Abrir `http://127.0.0.1:4321/`.

Repositorio: https://github.com/hinojosacajamariafernanda-cell/multiventas-jl

## Evidencias

- [Inicio y catálogo](docs/capturas/01-inicio-catalogo.png)
- [Ficha de producto](docs/capturas/02-ficha-producto.png)
- [Carrito](docs/capturas/03-carrito.png)
- [Entrega en la plataforma](docs/capturas/04-entrega-plataforma.png)
