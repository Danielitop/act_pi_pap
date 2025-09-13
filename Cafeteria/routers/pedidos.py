from fastapi import APIRouter, HTTPException
from typing import List  # Añadir este import
from database import pedidos_db, productos_db, next_pedido_id
from models import Pedido, PedidoCreate
from datetime import datetime

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

@router.get("/", response_model=List[Pedido])  # Corregido
def obtener_pedidos():
    return list(pedidos_db.values())

@router.get("/{pedido_id}", response_model=Pedido)
def obtener_pedido(pedido_id: int):
    if pedido_id not in pedidos_db:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    return pedidos_db[pedido_id]

@router.post("/", response_model=Pedido)
def crear_pedido(pedido: PedidoCreate):
    global next_pedido_id
    
    # Verificar que todos los productos existan
    for producto_id in pedido.productos:
        if producto_id not in productos_db:
            raise HTTPException(status_code=404, detail=f"Producto {producto_id} no encontrado")
    
    # Calcular total real
    total_real = sum(productos_db[pid].precio for pid in pedido.productos)
    
    nuevo_pedido = Pedido(
        id=next_pedido_id,
        fecha_creacion=datetime.now().isoformat(),
        total=total_real,
        **pedido.dict()
    )
    
    pedidos_db[next_pedido_id] = nuevo_pedido
    next_pedido_id += 1
    return nuevo_pedido

@router.put("/{pedido_id}/estado")
def actualizar_estado_pedido(pedido_id: int, estado: str):
    if pedido_id not in pedidos_db:
        raise HTTPException(status_code=404, detail="Pedido no encontrado")
    
    pedido = pedidos_db[pedido_id]
    pedido.estado = estado
    return {"message": "Estado actualizado correctamente"}

@router.get("/cliente/{email}", response_model=List[Pedido])  # Corregido
def obtener_pedidos_por_cliente(email: str):
    pedidos = [p for p in pedidos_db.values() if p.cliente_email.lower() == email.lower()]
    return pedidos