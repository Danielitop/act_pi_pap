from app.core.database import SessionLocal

# Esta función es un generador, y FastAPI sabe cómo usarlo.
# Proporciona una sesión de base de datos a un endpoint.
def get_db():
    db = SessionLocal()
    try:
        """
        try: ejemplo se crea una sesion en la base de datos (db = SessionLocal()) try es para capturar erores y si pasa un error, que no se detenga sino que realice otra cosa.
        """
        yield db  # Proporciona la sesión para que el endpoint la use
        """
        yield pausa la operacion temporalmente y devuelve un resultado
        """
    finally:
        db.close() # Cierra la conexión de la base de datos al finalizar
