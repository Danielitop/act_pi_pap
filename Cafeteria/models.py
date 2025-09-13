from pydantic import BaseModel
from typing import Optional, List  # Asegúrate de tener List importado
from enum import Enum

class Categoria(str, Enum):
    CAFE = "cafe"
    PASTELERIA = "pasteleria"
    BEBIDA = "bebida"
    SANDWICH = "sandwich"

class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    categoria: Categoria
    disponible: bool = True
    imagen: Optional[str] = None

    class Config:
        orm_mode = True

class ProductoCreate(ProductoBase):
    pass

class Producto(ProductoBase):
    id: int

class PedidoBase(BaseModel):
    cliente_nombre: str
    cliente_email: str
    productos: List[int]  # Aquí también se usa List
    total: float
    estado: str = "pendiente"

    class Config:
        orm_mode = True

class PedidoCreate(PedidoBase):
    pass

class Pedido(PedidoBase):
    id: int
    fecha_creacion: str