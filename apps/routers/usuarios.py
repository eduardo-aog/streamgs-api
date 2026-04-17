from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from apps.database import get_db
from apps.schemas.schemas import Usuario, UsuarioCreate
import apps.crud as crud

router = APIRouter(
    prefix="/usuarios",
    tags=["Usuarios"]
)

@router.get("/", response_model=List[Usuario])
def obtener_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_usuarios(db, skip=skip, limit=limit)

@router.get("/{id}", response_model=Usuario)
def obtener_usuario(id: int, db: Session = Depends(get_db)):
    usuario = crud.get_usuario(db, usuario_id=id)
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/", response_model=Usuario)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db, usuario)

@router.put("/{id}", response_model=Usuario)
def actualizar_usuario(id: int, usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud.update_usuario(db, id, usuario)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario

@router.delete("/{id}", response_model=Usuario)
def eliminar_usuario(id: int, db: Session = Depends(get_db)):
    db_usuario = crud.delete_usuario(db, id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return db_usuario
