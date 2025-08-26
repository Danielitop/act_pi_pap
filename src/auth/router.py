from fastapi import APIRouter
from . import service, schemas, models

router = APIRouter()

@router.get("/users")
def get_users():
    return {"message": "Listado de usuarios"}
