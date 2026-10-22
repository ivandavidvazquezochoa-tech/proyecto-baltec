import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Intenta usar la base de datos de la nube; si no existe, usa la de tu computadora
URL_NUBE = os.getenv("DATABASE_URL")
# ↓ REEMPLAZA ESTA LÍNEA CON LA URL EXACTA QUE YA TENÍAS ↓
URL_LOCAL = "postgresql://postgres:banano99012@localhost/baltec_db" 

SQLALCHEMY_DATABASE_URL = URL_NUBE or URL_LOCAL

# Ajuste automático requerido por plataformas de hosting en la nube (como Render o Heroku)
if SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()