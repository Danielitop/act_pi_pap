from typing import Dict, List
from models import Producto, Pedido

# Base de datos en memoria
productos_db: Dict[int, Producto] = {}
pedidos_db: Dict[int, Pedido] = {}
next_producto_id = 1
next_pedido_id = 1

# Datos iniciales de productos
productos_iniciales = [
    {
        "nombre": "Café Americano",
        "descripcion": "Café negro tradicional",
        "precio": 2.50,
        "categoria": "cafe",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1544787219-7f47ccb76574?w=400"
    },
    {
        "nombre": "Cappuccino",
        "descripcion": "Espresso con leche vaporizada y espuma",
        "precio": 3.50,
        "categoria": "cafe",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1561047029-3000c68339ca?w=400"
    },
    {
        "nombre": "Latte",
        "descripcion": "Café con leche cremoso",
        "precio": 3.00,
        "categoria": "cafe",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1572442388796-11668a67e53d?w=400"
    },
    {
        "nombre": "Croissant",
        "descripcion": "Panadería francesa tradicional",
        "precio": 2.00,
        "categoria": "pasteleria",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1555507036-ab794f24d6c7?w=400"
    },
    {
        "nombre": "Tarta de Manzana",
        "descripcion": "Deliciosa tarta casera",
        "precio": 3.50,
        "categoria": "pasteleria",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1562007908-859b4ba9a1a2?w=400"
    },
    {
        "nombre": "Té Verde",
        "descripcion": "Té verde orgánico",
        "precio": 2.00,
        "categoria": "bebida",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1559056199-641a0ac8b55e?w=400"
    },
    {
        "nombre": "Jugo de Naranja",
        "descripcion": "Jugo natural recién exprimido",
        "precio": 2.50,
        "categoria": "bebida",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1613478223719-2ab802602423?w=400"
    },
    {
        "nombre": "Sandwich Club",
        "descripcion": "Pollo, tocino, lechuga y tomate",
        "precio": 5.50,
        "categoria": "sandwich",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1502741224143-90386d7f8c82?w=400"
    },
    {
        "nombre": "Bagel con Queso Crema",
        "descripcion": "Bagel tostado con queso crema",
        "precio": 3.00,
        "categoria": "sandwich",
        "disponible": True,
        "imagen": "https://images.unsplash.com/photo-1586449480533-53f5e887adfd?w=400"
    }
]

# Inicializar base de datos
def init_db():
    global next_producto_id
    for producto_data in productos_iniciales:
        producto = Producto(id=next_producto_id, **producto_data)
        productos_db[next_producto_id] = producto
        next_producto_id += 1

init_db()