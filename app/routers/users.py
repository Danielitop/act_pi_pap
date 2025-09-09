#Propósito: Definir endpoints y manejar peticiones HTTP.

from fastapi import APIRouter, Depends
#es una herramienta de FastApi que organiza las rutas en mudulos separados.
#en lugar de meter todo los endpoints en main.py, creae "routes" n archivos distintos (por ejemplo, users.py, products.py) y luego los unes al proyecto.
from sqlalchemy.orm import Session
from app.crud import crud
from app.schemas import schemas
from app.models import models
from app.database.database import get_db

#DEFINICION DEL ROUTER
router = APIRouter(prefix="/users")
#crear APIRouter para manejar todas las rutas relacionadas con usuarios
#prefix= "/users" significa que todas las rutas de aqui dentro empezaran con /users
#EJEMPLO:
#POST/users/
#GET/Users/
#GET/users/{user_id}


#CREAR UN USUARIO
@router.post("/")
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    return crud.create_item(db, models.User, user)
#RUTA: POST/users/
#resibe: - una user que se valida con el esquema pydantic schemas.user
# - db:Session = Depends(get_db) -> inyecta la sesion de base de datos
#llama al CRUD generico: crud.create_item(db, models.User, user) -> esto insera el nuevo usuario en la tabla users

#OBTENER TODOS LOS USUARIOS
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return crud.get_all(db, models.User)
#RUTA: GET/users/
#Devuelve todos los usuarios de la base (SELECT * FROM users)

#OBTENER UN USUARIO POR ID
@router.get("/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_by_id(db, models.User, user_id)
#RUTA: GET/users/{user_id}
#- {user_id} es un parametro dinamico (ejemplo: /users/5)
#- bsucar en la base el usuario con ese id
# usa el CRUD generico get_by_id


#Responsabilidades: - Definir rutas HTTP - Manejar parámetros de petición - Validar entrada - Coordinar entre capas - Retornar respuestas HTTP