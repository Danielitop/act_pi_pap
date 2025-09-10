#Propósito: Configurar la conexión y sesión de base de datos.


from sqlalchemy import create_engine
#importa la funcion que crea el motor de concexion a la base de datos
#el engine es el onjeto que sabe como conectarse (por ejemplo a SQlite, postgreSQL, MySQL...etc)

from sqlalchemy.ext.declarative import declarative_base
#esto importa una base para empezar a crear la base de datos como modelos/tablas

from sqlalchemy.orm import sessionmaker
#importa una fabricante de sesiones: la sesion es el objeto que se usa para interactuar con la base de datos: agregar, consultar, actualizar o borrar datos

#en resumen:
#create_engine -> conecta con la base de datos
#declarative_base -> base para definir tus modelos/tablas
#sessionmaker -> fabrica sesiones para ejecutar consultas

#CONFIGURACION DE LA BASE DE DATOS
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
#"sqlite:///....." eso signifca que usaras SQLite y el archivo de la base se guardara en el mismo directorio (./) con el nombre test.db
#NOTA: podria cambiar segun el motor. si es postgreSQL o MySQL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
#engine es quien conecta o comunica con el motor de base de datos, (abrir conexiones, ejecutar SQL...)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#QUI SE DEFINE LA FABRICA DE SESIONES:
#autocommit = False   -> no se confirmas cambios automaticamente, (yo decido cuando usar el db.commit())

#autoflush = False    -> no se envia cambios automaticamente a la base en cada operacion, lo controlas tu.

#bind=engine         -> esta sesion usara el engine que conecta con tu base de datos.

Base = declarative_base()
#cuando quiera trabajar con la base de datos, crear una sesion (tambien prodria ser: db = SessionLocal())

#FUNCION PARA OBTENER SESION DE BD
def get_db():
    db = SessionLocal() # 1. crear una nueva sesion con la base de datos
    try:
        yield db        #2. devuelve la sesion para que la use la peticion
        #EN LUGAR DE USAR UN RETURN, SE USA YIELD POR QUE ESTA FUNCION SE USA COMO DEPENDENCIA EN FASTAPI. DE ESTA FORMA, FASTAPI "PRESTA" LA SEESION A LA RUTA MIENTRAS SE EJECUTA LA PETICION
    finally:
        db.close()      #3. al final, cierre la sesion (se ejecuta bien o con error)



#Responsabilidades: - Configurar la conexión a la base de datos - Crear el motor de SQLAlchemy - Gestionar sesiones de base de datos - Proporcionar la clase base para modelos