from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from apps.database import get_db
from apps.schemas.schemas import Genero, Artista
import apps.crud as crud

router = APIRouter(
    prefix="/catalogos",
    tags=["Catálogos"]
)

@router.get("/generos", response_model=List[Genero])
def obtener_generos(db: Session = Depends(get_db)):
    return crud.get_generos(db)

@router.get("/artistas", response_model=List[Artista])
def obtener_artistas(db: Session = Depends(get_db)):
    return crud.get_artistas(db)
