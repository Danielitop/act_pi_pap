from sqlalchemy import Colum, Integer, String
from sqlalchemy.orm import declarative_base
"""from sqlalchemy import Column, Integer, String:
con esto importamos las herramientas basicas para crear una tabla.
colum: clase principal para definir una columna
Integer: define que los datos en esa columna sera numeros enteros(como el id)
String: define que los datos sera texto(como usuario)

from sqlalchemy.orm import declarative_base: Esto es 
una función de SQLAlchemy que crea una "base" o una 
plantilla para todas tus clases de modelos.

"""

Base = declarative_base()

"""
Base = declarative_base()  : esto crea una intancia de la base.todas tus 
clases de modelos como (User) deben heredar de Base
"""

class User(Base):
    """
    class User(Base): aqui definimos llamada User. nota que usar hereda de 
    base. esto le dice a SQLAlchemy que esta clase debe ser mapeada a 
    una tabla en la base de datos
    

    __tablename__ = "users"  :esta linea es crucial. le decimos a SQLAlchemy que 
    el nombre de la tabla en la base de datos en este caso se usa "Users"  """

    __tablename__="users"

    id = Colum(Integer, print_key=True, index=True)
    Username = Colum(String,unique=True, index=True)
    password_hashed = Colum(String)
    role = Colum(String)

    """
    id = Column(Integer, primary_key=True, index=True) : aqui definimos la columna id.
    column: le dice python que esto es una columna de tabla

         interger: el tipo de dato es un numero entero

         primary_key=True: esto le dice a la base de datos que esta 
         columna es la clave primaria, osea la identificacion unico que cadaa fila de la tabla.

         index=True : esto crea un indice en la base de datos, lo que 
         hace que las busquedas por id sea mucho mas rapidas

    username = Column(String, unique=True, index=True) :    defines la 
    columna de username.
        String: el tipo de dato es texto
        unique= True : le dice a la base de datos que cada valor en esta 
        columan debe ser unico. dos usuarios no pueden tener el mismo nombre de usuario.

    password_hashed = Column(String) y role = Column(String): estas 
    lineaas defineen las columnas para la contraseña (ya se a hesheado, no en texto plano) 
    y para el rol de usuario, ambas como texto
    """