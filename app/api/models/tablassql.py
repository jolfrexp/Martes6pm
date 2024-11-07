from sqlalchemy import Column,Integer, String,Date,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Crear una instancia de la base para crear tablas
Base=declarative_base()

#Listado de modelos de la APLICACION
#USUARIO
class Usuario(Base):
    __tablename__='usuarios'
    id=Column(Integer, primary_key=True, autoincrement=True)
    nombre=Column(String(50))
    edad=Column(Integer)
    telefono=Column(String(12))
    correo=Column(String(20))
    contrasena=Column(String(10))
    fechaRegistro=Column(Date)
    ciudad=Column(String(50))
    facturas = relationship("Factura",back_populates="usuario")

#GASTO
class Gasto(Base):
    __tablename__ ='gastos' 
    id=Column(Integer,primary_key=True, autoincrement=True)
    monto=Column(Integer)
    descripcion=Column(String(75))
    categoria_id = Column(Integer,ForeignKey("categorias.id"))
    metodo_id =Column(Integer,ForeignKey("metodosDePago.id"))
    factura_id = Column(Integer,ForeignKey("facturas.id"))
    metodoDePago = relationship("MDP",back_populates="gastos")
    categoria =relationship("Categoria",back_populates="gastos")
    factura = relationship("Factura",back_populates="gastos")
    

#CATEGORIA
class Categoria(Base):
    __tablename__ = 'categorias'
    id=Column(Integer,primary_key=True, autoincrement=True)
    nombreCategoria=Column(String(50))
    descripcion=Column(String(75))
    fotoicono=Column(String(150))
    gastos = relationship("Gasto",back_populates="categoria")
    ingresos = relationship("Ingreso",back_populates="categoria")
#INGRESO
class Ingreso(Base):
    __tablename__ = 'ingresos'
    id=Column(Integer,primary_key=True, autoincrement=True)
    monto=Column(Integer)
    descripcion=Column(String(75))
    metodo_id =Column(Integer,ForeignKey("metodosDePago.id"))
    categoria_id = Column(Integer,ForeignKey("categorias.id"))
    factura_id = Column(Integer,ForeignKey("facturas.id"))
    factura = relationship("Factura",back_populates="ingresos")
    metodoDePago = relationship("MDP",back_populates="ingresos")
    categoria =relationship("Categoria",back_populates="ingresos")


#METODO DE PAGOS 
class MDP(Base):
    __tablename__ = 'metodosDePago'
    id=Column(Integer,primary_key=True, autoincrement=True)
    nombreMetodo=Column(String(50))
    descripcion=Column(String(100))
    gastos = relationship("Gasto",back_populates="metodoDePago")
    ingresos = relationship("Ingreso",back_populates="metodoDePago")

#FACTURA
class Factura(Base):
    __tablename__ = 'facturas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(Date,nullable = False)
    user_id = Column(Integer,ForeignKey("usuarios.id"))
    total  = Column(String(50),nullable =False)

    usuario = relationship("Usuario",back_populates="facturas")
    gastos = relationship("Gasto",back_populates="factura")
    ingresos = relationship("Ingreso",back_populates="factura")
    