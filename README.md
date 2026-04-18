# Streamgs API (Estructura de servicio de streaming de música)

> [!NOTE]
> **Materia:** Lenguaje de Programación  
> **Proyecto:** Streamgs  
> **Stack:** Python + FastAPI + SQLAlchemy + PostgreSQL / SQLite  

Streamgs es una API RESTful estructurada por capas construida con FastAPI que simula la gestión detrás de un servicio de streaming de música. Proporciona un sistema relacional completo para manejar Artistas, Canciones, Álbumes, Playlists, Géneros y el CRUD central para Usuarios.

## 🚀 Requisitos Previos

- **Python 3.10+** (Recomendado)
- Opcional: Servidor PostgreSQL instalado (En local se usa SQLite por defecto).

## 🛠️ Instalación y Configuración Local

Sigue estos pasos para arrancar el proyecto de manera local en tu computadora:

1. **Clona o ubícate en el directorio del proyecto:**
   ```bash
   cd proyecto-fastapi
   ```

2. **Crea y activa un Entorno Virtual** (muy recomendado):
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Linux/Mac
   # En Windows: .venv\Scripts\activate
   ```

3. **Instala las dependencias necesarias:**
   Asegúrate de instalar los paquetes principales desde el archivo de requerimientos:
   ```bash
   pip install -r requirements.txt
   
   # Si falla por problemas del driver de postgres al compilar, instala las directas temporales:
   pip install fastapi uvicorn sqlalchemy pydantic-settings python-dotenv "pydantic[email]"
   ```

4. **Variables de Entorno (.env):**
   El archivo `.env` en la raíz ya está configurado para desarrollo local:
   ```env
   DATABASE_URL=sqlite:///./streamgs.db
   ```
   *Nota: Cuando hagas el despliegue a Render o Railway, cambiarás este valor a tu string de PostgreSQL.*

## ▶️ Ejecución del Servidor

Una vez instalado, corre el servidor web interno:

```bash
uvicorn apps.main:app --reload
```
> El flag `--reload` hace que el servidor se reinicie automáticamente cada vez que edites el código.

Si todo es correcto, la terminal mostrará:
`Uvicorn running on http://127.0.0.1:8000`

## 📖 Uso de la API (Documentación Interactiva)

No hace falta probar a ciegas. FastAPI genera documentación gráfica automática con la cual puedes probar métodos `GET`, `POST`, `PUT`, `DELETE`.

1. Abre tu navegador y dirígete a: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
2. Encontrarás la interfaz de **Swagger**.
3. Haz clic en cualquier endpoint (por ejemplo `/usuarios/`), luego en el botón **"Try it out"** y finalmente en **"Execute"**. 

**Seed Automático:**
*¡No tienes que cargar bases de datos manuales!* La primera vez que el servidor corre, autogenerará los catálogos insertando 10 artistas falsos, canciones para sus álbumes y 6 géneros musicales que puedes consumir en los registros.

## 📁 Archivos de referencia
Si buscas una comprensión lógica más profunda revisa estos archivos que viven en la raíz de este proyecto:
- `documentacion_api.md`: Detalles precisos de qué enviar a cada ruta específica.
- `schema.sql`: Estructura y tabla de entidades que gobierna esta API.
