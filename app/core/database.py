#este sera el corazon de la base de datos
"""
la capeta core su proposito es almacenar archivos y modulos que contiene la logica central y fundamental de una aplicaciones, es como el cerebro  o el nucleo del proyecto

que suele contener?:
contiene componentes que son crusciales para el funcionamiento del sistema, que no pertenece especificamente aplicacion , como la interfaz de usuario o una funcionalidad particular.

- configuraciones: archivos con variables de entorno, ajustes de base de datos o claves de API.

-concectores: modulos que establecen la conexion con servicios externos, como bases de datos APIs o sistemas de cache. en mi codigo por ejemplo el archivo esta relacionado con SQLAlchemy (como el engine o la sesionLOcal) se ubican perfectamente aqui.

-servicios compartidos: funciones o clases que se usan en multiples partes de la aplicacion, como utilidades para el manejo de fechas, validacion de datos o encriptacion de contraseña.

-modelos de datos: las clases que definen la estructura de los datos que se guardaran en la base de datos, auqnue a veces esto se ubican en una carpeta separada llamda models
"""

from sqlalchemy import create_engine
"""
es una funcion que crea una instancia de un motor de base de datos. este motor actua como un punto de conexion para todas las operaciones que hara en la base de datos. en terminos simples, es lo que te permite "hablar" con la base de datos.
"""
from sqlalchemy.orm import sessionmaker
"""
es una clase que crea una fabrica de sesiones. una sesion es la froma principal de interactuar con la base de datos: te permite hacer consultas, agregar datos, actualizarlos y eliminarlos. la fabrica de sesiones es como una plantilla para crear esras sesiones.
"""
from sqlalchemy.ext.declarative import declarative_base
"""
es una funcion que retorna una clase base. todo los modelos de la tablas (por ejemplo, una clase Usuario o Producto) deben heredar de esta clase base. al hacerlo, le das a tus clases la capacidad de mapearse automaticamente a tablas en la base de datos. es el corazon de la parte "declarativa" de SQLAlchemy, donde describes tus modelos da datos como clases de python
"""

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
"""
declara una contante que contiene la URL de la base de datos. en este caso, se esta usando SQLite, y el archivo de la base de datos se llamara sql_app.db y se creara en el mismo direcotio donde se ejecute el script
"""

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
"""
 Crea una instancia de Engine usando la URL definida. Este Engine es el punto de partida para todas las conexiones con la base de datos. La opción connect_args={"check_same_thread": False} es específica para SQLite y le permite manejar múltiples hilos, lo que es común en aplicaciones web como las que usa FastAPI, evitando errores de concurrencia.
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
crea uan clase de sesion llamada sesionLocal. crea una clase de sesion llamada sesionLocal. esta clase es un contructor de sesiones se encargara de gestionar las transacciones de la base de datos. los argumentos autocommit = False y autoflush = False controla el comportamietno de las transacciones, asegurando que los cambios no se guarden automaticamente y que se puedan agrupar en una sola transaccion. el arguemtno bind=engine vincula esta clase de sesion al motor que se creo anteriormente 
"""

Base = declarative_base()

"""
llama a la funcion (declarative_base()) para crear una clase base declarativa. esta clase, llamada Base, es de la que heredan los modelos (Tablas) de la apliacion. al heredar de Base, los modelos obtienen la funcionalidad necesaria para mapear clases de python a tablas de la base de datos
"""