from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    activo = Column(Boolean, default=True)

# --- NUEVAS TABLAS PARA LA DEMO ---

class Producto(Base):
    __tablename__ = "productos_v2" # Renombrado para crear la tabla desde cero
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    descripcion = Column(String)
    precio = Column(Float)
    stock = Column(Integer)
    imagen_url = Column(String, default="https://via.placeholder.com/400x300?text=SIN+FOTO") # <-- ESTA LÍNEA FALTABA

class Pedido(Base):
    __tablename__ = "pedidos"
    id = Column(Integer, primary_key=True, index=True)
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer)
    total = Column(Float)

class Prospecto(Base):
    __tablename__ = "prospectos"
    id = Column(Integer, primary_key=True, index=True)
    nombre_cliente = Column(String)
    email_cliente = Column(String)
    telefono = Column(String)
    equipo_interes = Column(String)