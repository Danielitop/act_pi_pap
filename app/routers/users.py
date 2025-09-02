"""
routers es el encarfade denlacar los usuarios a el archivo principal (main.py) el es encargadi de manejar las peticiones HTTP, y para todo lo relacionado con los usuarios como el registro o la obetencion de datos.
"""

from fastapi import APIRouter, Depends, HTTPException, status
"""
esta linea importa las herramientas principales de FasAPI
    -APIRouter: es la clase principal que se usa para organizar las rutas de la API en modulos separados.

    -depends: se usa para manejar dependencias y manejo de base de datos.

    -HTTPEcception: esto maneja los errores del HTTP

    -status: es para manejar las respuestaas ya que contiene el codigo de estado HTTP
"""
from sqlalchemy.orm import Session
#trae las sesiones de SQLAlchemy, que representa una sesion de base de datos.

#TRAE LOS OTROS MODULOS
from app.core.dependencies import get_db
from app.models import models
from app.schemas import schemas

# Create an API router
router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_users(db: Session = Depends(get_db)):
    return {"message": "Users endpoint is working!"}