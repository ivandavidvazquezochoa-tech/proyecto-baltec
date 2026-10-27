from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    activo = Column(Boolean, default=True)

# --- NUEVAS TABLAS PARA LA DEMO ---

class Producto(Base):
    __tablename__ = "productos_v3" # <-- Corregido para evitar errores
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    categoria = Column(String, index=True) # <-- NUEVO: Para filtrar por extractores, inyectores, etc.
    precio = Column(Float)
    stock = Column(Integer)
    imagen_url = Column(String, default="https://via.placeholder.com/400x300?text=SIN+FOTO") 
    es_personalizable = Column(Boolean, default=False) # <-- NUEVO: Interruptor para piezas a la medida
    opciones_personalizacion = Column(Text, nullable=True) # <-- NUEVO: Texto de las modificaciones posibles

class Pedido(Base):
    __tablename__ = "pedidos_v3"
    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos_v3.id")) # <-- Apuntando a la nueva tabla
    cantidad = Column(Integer)
    total = Column(Float)

class Prospecto(Base):
    __tablename__ = "prospectos"
    id = Column(Integer, primary_key=True, index=True)
    nombre_cliente = Column(String)
    email_cliente = Column(String)
    telefono = Column(String)
    equipo_interes = Column(String)