from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from routers import productos, pedidos

app = FastAPI(
    title="API Cafetería Delicioso",
    description="API para gestión de productos y pedidos de cafetería",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Servir archivos estáticos del frontend
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Incluir routers
app.include_router(productos.router)
app.include_router(pedidos.router)

@app.get("/")
def root():
    return {
        "message": "Bienvenido a la API de la Cafetería Delicioso",
        "endpoints": {
            "productos": "/productos",
            "pedidos": "/pedidos",
            "documentación": "/docs",
            "frontend": "/static/index.html"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy", "total_productos": len(productos.productos_db)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)