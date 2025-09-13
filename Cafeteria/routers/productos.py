from fastapi import APIRouter, HTTPException
from typing import List  # ¡Falta este import!
from database import productos_db, next_producto_id
from models import Producto, ProductoCreate

router = APIRouter(prefix="/productos", tags=["productos"])

@router.get("/", response_model=List[Producto])  # Corregido
def obtener_productos():
    return list(productos_db.values())

@router.get("/{producto_id}", response_model=Producto)
def obtener_producto(producto_id: int):
    if producto_id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return productos_db[producto_id]

@router.get("/categoria/{categoria}", response_model=List[Producto])  # Corregido
def obtener_productos_por_categoria(categoria: str):
    productos = [p for p in productos_db.values() if p.categoria == categoria]
    return productos

@router.post("/", response_model=Producto)
def crear_producto(producto: ProductoCreate):
    global next_producto_id
    nuevo_producto = Producto(id=next_producto_id, **producto.dict())
    productos_db[next_producto_id] = nuevo_producto
    next_producto_id += 1
    return nuevo_producto

@router.put("/{producto_id}", response_model=Producto)
def actualizar_producto(producto_id: int, producto: ProductoCreate):
    if producto_id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    producto_actualizado = Producto(id=producto_id, **producto.dict())
    productos_db[producto_id] = producto_actualizado
    return producto_actualizado

@router.delete("/{producto_id}")
def eliminar_producto(producto_id: int):
    if producto_id not in productos_db:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    del productos_db[producto_id]
    return {"message": "Producto eliminado correctamente"}