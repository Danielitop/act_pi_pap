#Propósito: Inicializar y configurar la aplicación FastAPI.

from fastapi import FastAPI
from app.database.database import engine
from app.models import models
from app.routers import users, products, orders

#crear tabla en la base de datos
models.Base.metadata.create_all(bind=engine)

#crear aplicacion FastAPI
app = FastAPI()

#incluir routers
app.include_router(users.router)
app.include_router(products.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"mensage": "API simple"}

#Responsabilidades: - Inicializar FastAPI - Configurar la aplicación - Registrar routers - Crear tablas de base de datos