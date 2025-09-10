# Propósito: Manejar las rutas relacionadas con los productos.
# Define los endpoints para operaciones de productos.

from fastapi import APIRouter

# Crea el router de productos
router = APIRouter(prefix="/products", tags=["Products"])

# Endpoint de ejemplo para obtener todos los productos
@router.get("/")
def get_products():
    return {"message": "Listado de productos"}