#Propósito: Definir la estructura de las tablas de base de datos.



from sqlalchemy import Column, Integer, String, Float
#esto importa tipos de columnas que se usan para definir los campos de las tablas (modelos) en SQLAlchemy

#LISTA
#column: sirve para definir una columna dentro de un modelo(tabla). se usa como: id = Column(Integer, primary_key=True)

#Interger -> tipo de datos entero(int) en SQL
#calle = column(Interger)

#String  -> tipo de dato texto
#pais = column(String(50)) (hasta 50 caracteres)

#Float  -> tipo de dato decimal
#altura = column(Float)


from app.database.database import Base
#importamos el modulo de data base

class User(Base):
    __tablename__ = "users"
    id = Column (Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

class product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

class Order(Base):
    __tablaname__ = "orders"
    id = Column(Integer, primary_key= True)
    User_id = Column(Integer)
    product_id = Column(Integer)
    quantity = Column(Integer) 

#Responsabilidades: - Definir estructura de tablas - Especificar tipos de datos - Establecer relaciones entre tablas - Mapear objetos Python a tablas SQL