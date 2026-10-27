from pydantic import BaseModel
from typing import Optional

class ProductoBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    categoria: str 
    imagen_url: Optional[str] = "https://via.placeholder.com/400x300?text=SIN+FOTO"
    es_personalizable: bool = False 
    opciones_personalizacion: Optional[str] = None 

class ProductoCreate(BaseModel):
    nombre: str
    descripcion: str | None = None
    categoria: str 
    imagen_url: str = "https://via.placeholder.com/400x300?text=SIN+FOTO"
    es_personalizable: bool = False 
    opciones_personalizacion: str | None = None 

class ProductoResponse(ProductoBase):
    id: int
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