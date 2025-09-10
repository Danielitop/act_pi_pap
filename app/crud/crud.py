#Propósito: Implementar operaciones de base de datos.

from sqlalchemy.orm import Session
#lo que importa el session es un molde con toda las modificaciones clasicas de usuario osea.

# Hacer consultas (SELECT).
# Insertar registros (INSERT).
# Actualizar (UPDATE).
# Eliminar (DELETE).

#en terminos cortos es como un "puente" entre los modelos python (ORM) y la base de datos real.

from models import models
from schemas import schemas

# 1. obtiene todos los registros

def get_all(db: Session, model):
    return db.query(model).all()

# -db: Session -> la sesion activas con la base de datos
# -model       -> la tabla/modelo de SQLAlchemy (ej: USer, Product)
# HACE UN SELECT * FROM <tabla> y devuelve todo los registros en forma de lista de objetos ORM

# 2. Obtener un registro por ID
def get_by_id(db: Session, model, item_id: int):
    return db.query(model).filter(model.id == item_id).first()
# - model.id == item_id   -> aplica un filtro en la consulta
# - .firs()  -> devuelve el primer resultado o None si no existe
#SE PUEDE HACER UN SELECT * FROM  <tabla> WHERE id = item_id LIMIT 1


# 3. Crear un nuevo registro
def create_item(db: Session, model, item_data):
    db_item = model(**item_data.dict(exclude={'id'}))
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#item_data.dict(exclude={'id'})   -> convierte el modelo Pydantic en un diccionario, pero excluye el campo id (porque normalmente es autogenerado en la BD).
#por ejemplo: {"name": "Ana", "email": "ana@mail.com"}

#db_item = model(**...) → crea una instancia del modelo SQLAlchemy (User, Product, etc.) con esos datos.

#db.add(db_item) → lo añade a la sesión.

#db.commit() → guarda los cambios en la base de datos (ejecuta el INSERT).

#db.refresh(db_item) → actualiza el objeto con los datos que asignó la BD (ej: el id autoincremental).

#return db_item → devuelve el objeto creado, ya con su id.



#Responsabilidades: - Ejecutar consultas SQL - Manejar transacciones - Implementar lógica de negocio - Abstraer operaciones de base de datos