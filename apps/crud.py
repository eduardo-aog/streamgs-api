from sqlalchemy.orm import Session
from apps.models.models import Usuario, Genero, Artista, Album, Cancion
from apps.schemas.schemas import UsuarioCreate

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        genero_preferido_id=usuario.genero_preferido_id,
        artista_favorito_id=usuario.artista_favorito_id
    )
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario_actualizado: UsuarioCreate):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db_usuario.nombre = usuario_actualizado.nombre
        db_usuario.email = usuario_actualizado.email
        db_usuario.genero_preferido_id = usuario_actualizado.genero_preferido_id
        db_usuario.artista_favorito_id = usuario_actualizado.artista_favorito_id
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
    return db_usuario

def get_generos(db: Session):
    return db.query(Genero).all()

def get_artistas(db: Session):
    return db.query(Artista).all()

def seed_database(db: Session):
    # Si ya hay generos o artistas, no hacemos nada
    if db.query(Genero).first() or db.query(Artista).first():
        return

    print("INFO: BD inicializada vacía. Insertando Seed de datos...")

    # Insertamos géneros
    generos = ["Rock", "Pop", "Jazz", "Hip Hop", "Clásica", "Electrónica"]
    db_generos = []
    for g_name in generos:
        g = Genero(nombre=g_name)
        db.add(g)
        db_generos.append(g)
    db.commit()

    # Insertamos 10 artistas, cada uno con un album y 5 canciones
    for i in range(1, 11):
        artista = Artista(nombre=f"Artista {i}", biografia=f"Bio de Artista {i}", oyentes_mensuales=1000 * i)
        db.add(artista)
        db.commit()
        db.refresh(artista)

        album = Album(titulo=f"Album Debut {i}", artista_id=artista.id)
        db.add(album)
        db.commit()
        db.refresh(album)

        for j in range(1, 6):
            cancion = Cancion(
                titulo=f"Cancion {j} de Artista {i}",
                duracion_segundos=180 + j * 10,
                album_id=album.id,
                genero_id=db_generos[i % len(db_generos)].id
            )
            db.add(cancion)
        db.commit()
