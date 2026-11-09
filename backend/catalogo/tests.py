# Pruebas de los endpoints. Ejecutar:  python manage.py test
import json

from django.test import SimpleTestCase


class ApiTests(SimpleTestCase):
    def test_lista_productos(self):
        r = self.client.get("/api/productos/")
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(r.json()), 6)

    def test_crea_pedido(self):
        cuerpo = {"metodo_entrega": "ENVIO_SHALOM", "items": [{"producto_id": 1, "cantidad": 2}]}
        r = self.client.post("/api/pedidos/", json.dumps(cuerpo), content_type="application/json")
        self.assertEqual(r.status_code, 201)
        self.assertEqual(r.json()["total"], 30.0)
        self.assertEqual(r.json()["estado"], "PENDIENTE")

    def test_rechaza_stock_excesivo(self):
        cuerpo = {"metodo_entrega": "RECOJO", "items": [{"producto_id": 6, "cantidad": 99}]}
        r = self.client.post("/api/pedidos/", json.dumps(cuerpo), content_type="application/json")
        self.assertEqual(r.status_code, 400)

    def test_rechaza_carrito_vacio(self):
        cuerpo = {"metodo_entrega": "RECOJO", "items": []}
        r = self.client.post("/api/pedidos/", json.dumps(cuerpo), content_type="application/json")
        self.assertEqual(r.status_code, 400)
