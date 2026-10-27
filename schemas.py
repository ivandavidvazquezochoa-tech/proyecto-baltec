from pydantic import BaseModel
from typing import Optional

# ... (deja lo que ya tienes de UsuarioCreate y UsuarioResponse) ...

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    categoria: str # <-- NUEVO
    precio: float
    stock: int
    imagen_url: Optional[str] = "https://via.placeholder.com/400x300?text=SIN+FOTO"
    es_personalizable: bool = False # <-- NUEVO
    opciones_personalizacion: Optional[str] = None # <-- NUEVO

class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str | None = None
    categoria: str # <-- NUEVO
    precio: float
    stock: int
    imagen_url: str = "https://via.placeholder.com/400x300?text=SIN+FOTO"
    es_personalizable: bool = False # <-- NUEVO
    opciones_personalizacion: str | None = None # <-- NUEVO

class ProductoResponse(ProductoBase):
    id: int
    class Config:
        from_attributes = True

class PedidoCreate(BaseModel):
    producto_id: int
    cantidad: int

class PedidoResponse(BaseModel):
    id: int
    producto_id: int
    cantidad: int
    total: float
    class Config:
        from_attributes = True

class ProspectoCreate(BaseModel):
    nombre_cliente: str
    email_cliente: str
    telefono: str
    equipo_interes: str

class ProspectoResponse(ProspectoCreate):
    id: int
    class Config:
        from_attributes = True