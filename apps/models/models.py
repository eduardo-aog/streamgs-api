from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, DateTime, Date
from sqlalchemy.orm import relationship
from datetime import datetime
from apps.database import Base

class Genero(Base):
    __tablename__ = 'generos'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), unique=True, nullable=False)

    usuarios = relationship("Usuario", back_populates="genero_preferido")
    canciones = relationship("Cancion", back_populates="genero")

class Artista(Base):
    __tablename__ = 'artistas'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False, index=True)
    biografia = Column(Text, nullable=True)
    oyentes_mensuales = Column(Integer, default=0)
    creado_en = Column(DateTime, default=datetime.utcnow)

    albumes = relationship("Album", back_populates="artista")
    fans = relationship("Usuario", back_populates="artista_favorito")

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    genero_preferido_id = Column(Integer, ForeignKey('generos.id', ondelete='SET NULL'), nullable=True)
    artista_favorito_id = Column(Integer, ForeignKey('artistas.id', ondelete='SET NULL'), nullable=True)
    creado_en = Column(DateTime, default=datetime.utcnow)

    genero_preferido = relationship("Genero", back_populates="usuarios")
    artista_favorito = relationship("Artista", back_populates="fans")
    playlists = relationship("Playlist", back_populates="usuario")

class Album(Base):
    __tablename__ = 'albumes'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False)
    fecha_lanzamiento = Column(Date, nullable=True)
    artista_id = Column(Integer, ForeignKey('artistas.id', ondelete='CASCADE'), nullable=False)
    creado_en = Column(DateTime, default=datetime.utcnow)

    artista = relationship("Artista", back_populates="albumes")
    canciones = relationship("Cancion", back_populates="album")

class Playlist(Base):
    __tablename__ = 'playlists'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    descripcion = Column(Text, nullable=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id', ondelete='CASCADE'), nullable=False)
    es_publica = Column(Boolean, default=True)
    creado_en = Column(DateTime, default=datetime.utcnow)

    usuario = relationship("Usuario", back_populates="playlists")
    canciones_asociadas = relationship("PlaylistCancion", back_populates="playlist")

class Cancion(Base):
    __tablename__ = 'canciones'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(255), nullable=False, index=True)
    duracion_segundos = Column(Integer, nullable=False)
    album_id = Column(Integer, ForeignKey('albumes.id', ondelete='CASCADE'), nullable=False)
    genero_id = Column(Integer, ForeignKey('generos.id', ondelete='SET NULL'), nullable=True)
    creado_en = Column(DateTime, default=datetime.utcnow)

    album = relationship("Album", back_populates="canciones")
    genero = relationship("Genero", back_populates="canciones")
    playlists_asociadas = relationship("PlaylistCancion", back_populates="cancion")

class PlaylistCancion(Base):
    __tablename__ = 'playlist_canciones'
    playlist_id = Column(Integer, ForeignKey('playlists.id', ondelete='CASCADE'), primary_key=True)
    cancion_id = Column(Integer, ForeignKey('canciones.id', ondelete='CASCADE'), primary_key=True)
    posicion = Column(Integer, nullable=True)
    agregado_en = Column(DateTime, default=datetime.utcnow)

    playlist = relationship("Playlist", back_populates="canciones_asociadas")
    cancion = relationship("Cancion", back_populates="playlists_asociadas")
