from pydantic import BaseModel
from typing import Optional

# ... (deja lo que ya tienes de UsuarioCreate y UsuarioResponse) ...

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    precio: float
    stock: int

class ProductoCreate(ProductoBase):
    pass

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