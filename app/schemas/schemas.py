#Propósito: Validar y serializar datos de entrada y salida.


from pydantic import BaseModel
#IMPORTA la clase base de pydantic, que se usa en FastAPI (y otros proyectos) para definir modelos da datos

#   ¿QUE ES UN  BaseModel EN PYDACTIC?
# es como un molde ya hecho que valida y estructura datos que entran o salen de la API.
#       - Cuando el cliente envía datos (ejemplo: un POST con JSON), Pydantic valida que cumpla con los tipos que declaraste.
#       -Cuando respondes datos, puedes usarlo para devolver respuestas con una forma consistente.

class User(BaseModel):
    id: int = None #aqui el None significa que si no se envia ese campo, su valor por defecto sera nulo
    name: str
    email: str

    class Config:
        from_attributes = True #bueno en el modulo de models.py usamos es el lenguaje de SQLAlchemy o mas conocido como instancias ORM. y las convierta en JSON automaticamente.    ES UN TIPO DE TRADUCION DE COMPATIBILIDAD ENTRE FastAPI y SQLAlchemy.
    
class product(BaseModel):
    id: int = None
    name: str
    price: float

    class Config:
        from_attributes = True

class Order(BaseModel):
    id: int = None
    user_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True

#Responsabilidades: - Validar datos de entrada - Serializar datos de salida - Documentar la estructura de la API - Convertir entre formatos (JSON ↔ Python)