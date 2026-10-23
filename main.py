from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.responses import HTMLResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy.orm import Session
import models, schemas
import secrets
from database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Baltec API")

security = HTTPBasic()

def verificar_admin(credentials: HTTPBasicCredentials = Depends(security)):
    # Aquí se definen credenciales (se pueden cambiar luego)
    usuario_correcto = secrets.compare_digest(credentials.username, "admin")
    password_correcto = secrets.compare_digest(credentials.password, "baltec2026")
    
    if not (usuario_correcto and password_correcto):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales incorrectas",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ESTA RUTA AHORA ES LA PRINCIPAL Y MUESTRA LA TIENDA PÚBLICA (SIN CONTRASEÑA)
@app.get("/", response_class=HTMLResponse)
def leer_tienda():
    try:
        with open("tienda.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Archivo tienda.html no encontrado.</h1>"

# ESTA RUTA AHORA ES /negocio Y ESTÁ PROTEGIDA CON CONTRASEÑA PARA EL ADMINISTRADOR
@app.get("/negocio", response_class=HTMLResponse)
def leer_interfaz(username: str = Depends(verificar_admin)):
    try:
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "<h1>Archivo index.html no encontrado.</h1>"
    
# --- RUTAS DE PRODUCTOS ---
@app.post("/productos/", response_model=schemas.ProductoResponse)
def crear_producto(producto: schemas.ProductoCreate, db: Session = Depends(get_db)):
    nuevo_producto = models.Producto(**producto.model_dump())
    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)
    return nuevo_producto

@app.get("/productos/", response_model=list[schemas.ProductoResponse])
def leer_productos(db: Session = Depends(get_db)):
    return db.query(models.Producto).all()

# --- RUTAS DE PEDIDOS ---
@app.post("/pedidos/", response_model=schemas.PedidoResponse)
def crear_pedido(pedido: schemas.PedidoCreate, db: Session = Depends(get_db)):
    # Buscamos el producto
    producto = db.query(models.Producto).filter(models.Producto.id == pedido.producto_id).first()
    
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
        
    if producto.stock < pedido.cantidad:
        raise HTTPException(status_code=400, detail="Stock insuficiente en el inventario")
    
    # ¡Magia! Restamos el stock automáticamente
    producto.stock -= pedido.cantidad
    
    total_calculado = producto.precio * pedido.cantidad
    
    nuevo_pedido = models.Pedido(
        producto_id=pedido.producto_id, 
        cantidad=pedido.cantidad, 
        total=total_calculado
    )
    db.add(nuevo_pedido)
    db.commit()
    db.refresh(nuevo_pedido)
    return nuevo_pedido

@app.get("/pedidos/", response_model=list[schemas.PedidoResponse])
def leer_pedidos(db: Session = Depends(get_db)):
    return db.query(models.Pedido).all()

# --- NUEVA RUTA PARA ELIMINAR ---
@app.delete("/productos/{producto_id}")
def eliminar_producto(producto_id: int, db: Session = Depends(get_db)):
    producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    
    db.delete(producto)
    db.commit()
    return {"mensaje": "Producto eliminado exitosamente"}

# --- RUTAS DE PROSPECTOS / COTIZACIONES ---
@app.post("/prospectos/", response_model=schemas.ProspectoResponse)
def crear_prospecto(prospecto: schemas.ProspectoCreate, db: Session = Depends(get_db)):
    nuevo_prospecto = models.Prospecto(**prospecto.model_dump())
    db.add(nuevo_prospecto)
    db.commit()
    db.refresh(nuevo_prospecto)
    return nuevo_prospecto

@app.get("/prospectos/", response_model=list[schemas.ProspectoResponse])
def leer_prospectos(db: Session = Depends(get_db)):
    return db.query(models.Prospecto).order_by(models.Prospecto.id.desc()).all()