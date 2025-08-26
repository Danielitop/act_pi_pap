from fastapi import FastAPI
from core import config, database, exceptions  # Importas tu configuración y lógica base
from auth import router as auth_router          # Importas el router del módulo auth

# Inicializas la app
app = FastAPI(
    title="Mi Proyecto FastAPI",
    description="API modular con FastAPI",
    version="1.0.0"
)

# Conectar base de datos al iniciar la app
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Incluir routers
app.include_router(auth_router.router, prefix="/auth", tags=["Auth"])

# Manejo de excepciones personalizadas (si tienes en core/exceptions.py)
exceptions.register_exceptions(app)

# Ruta principal
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API 🚀"}
