from contextlib import asynccontextmanager
from fastapi import FastAPI
from apps.database import engine, Base, SessionLocal
from apps.routers.usuarios import router as router_usuarios
from apps.routers.catalogos import router as router_catalogos
from apps.crud import seed_database

# Lifespan para ejecutar tareas al arrancar y finalizar
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Crear las tablas (si no existen)
    Base.metadata.create_all(bind=engine)
    
    # 2. Levantar sesión inicial para sembrar la DB
    db = SessionLocal()
    try:
        seed_database(db)
    finally:
        db.close()
    
    yield
    # Limpieza en apagado si es necesaria

app = FastAPI(
    title="Streamgs API",
    description="API para el servicio de streaming Streamgs",
    version="1.0.0",
    lifespan=lifespan
)

# Registrando Routers
app.include_router(router_usuarios)
app.include_router(router_catalogos)

@app.get("/")
def inicio():
    return {"mensaje": "Streamgs API corriendo mediante capas correctamente"}
