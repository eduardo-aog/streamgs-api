from typing import List, Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime, date

class GeneroBase(BaseModel):
    nombre: str

class GeneroCreate(GeneroBase):
    pass

class Genero(GeneroBase):
    id: int

    class Config:
        from_attributes = True

class ArtistaBase(BaseModel):
    nombre: str
    biografia: Optional[str] = None
    oyentes_mensuales: Optional[int] = 0

class ArtistaCreate(ArtistaBase):
    pass

class Artista(ArtistaBase):
    id: int
    creado_en: datetime

    class Config:
        from_attributes = True

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    genero_preferido_id: Optional[int] = None
    artista_favorito_id: Optional[int] = None

class UsuarioCreate(UsuarioBase):
    pass

class Usuario(UsuarioBase):
    id: int
    creado_en: datetime
    # Se podría incluir el artista y genero si usamos esquemas anidados
    artista_favorito: Optional[Artista] = None
    genero_preferido: Optional[Genero] = None

    class Config:
        from_attributes = True

# --- CANCION ---
class CancionBase(BaseModel):
    titulo: str
    duracion_segundos: int
    album_id: int
    genero_id: Optional[int] = None

class CancionCreate(CancionBase):
    pass

class Cancion(CancionBase):
    id: int
    creado_en: datetime

    class Config:
        from_attributes = True
