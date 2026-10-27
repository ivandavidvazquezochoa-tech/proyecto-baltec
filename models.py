from sqlalchemy import Column, Integer, String, Boolean, Text
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    activo = Column(Boolean, default=True)

class Producto(Base):
    __tablename__ = "productos_v4" 
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    categoria = Column(String, index=True) 
    imagen_url = Column(String, default="https://via.placeholder.com/400x300?text=SIN+FOTO") 
    es_personalizable = Column(Boolean, default=False) 
    opciones_personalizacion = Column(Text, nullable=True) 

class Prospecto(Base):
    __tablename__ = "prospectos"
    id = Column(Integer, primary_key=True, index=True)
    nombre_cliente = Column(String)
    email_cliente = Column(String)
    telefono = Column(String)
    equipo_interes = Column(String)