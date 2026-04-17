# Análisis de la Aplicación FastAPI (`app-maria/app`)

Este archivo documenta el funcionamiento general de la API construida con FastAPI en la carpeta `app-maria/app`, su configuración de base de datos y la función del archivo en el que se listan las dependencias.

## 1. ¿Qué hace el código en la carpeta `app`?

La carpeta es el núcleo de una API RESTful para la gestión de usuarios. Sigue una arquitectura limpia y separada por responsabilidades comunes en aplicaciones de FastAPI:

*   **`main.py`**: Es el punto de entrada de la aplicación. Configura la instancia de la aplicación FastAPI, invoca a SQLAlchemy para crear las tablas de base de datos al inicio de la ejecución e incluye todos los enrutadores (como el de `usuarios`). También tiene una ruta básica en la raíz (`/`) para verificar que la API esté viva.
*   **`config.py`**: Maneja las configuraciones globales utilizando `pydantic_settings`. Aquí se especifica la cadena de conexión de la base de datos (`DATABASE_URL`), la cual puede ser configurada dinámicamente mediante un archivo oculto o variables de entorno (`.env`).
*   **`database.py`**: Su responsabilidad es centralizar la comunicación de bajo nivel con la base de datos mediante SQLAlchemy.
*   **`crud.py`** *(Create, Read, Update, Delete)*: Contiene las funciones de lógica de negocio o de repositorio. Se encarga de usar una sesión de la base de datos (`Session`) para manipular registros: obtener todos los usuarios, buscar por ID o email, crear usuarios, editar y eliminar.
*   **Directorios Internos (`models`, `schemas`, `routers`)**: Aunque no se analizó el código a dentro al detalle, sabemos que: 
    *   `models/` define la estructura de las tablas en nuestra base de datos.
    *   `schemas/` establece estructuras de validación para los datos (usando Pydantic) enviados por los clientes.
    *   `routers/` define las diferentes URL o rutas habilitadas para interactuar con la parte de negocio.

## 2. Conexión de la Base de Datos

El sistema usa **PostgreSQL** a través del ORM **SQLAlchemy**. El flujo de conexión funciona de la siguiente forma:

1.  **Definición de Credenciales (`config.py`)**: Se guarda la ruta hacia la BD. El string por defecto es `"postgresql://usuario:password@localhost/mibd"`, pero está preparado para cargarse desde un archivo `.env`.
2.  **Creación del Motor y la Sesión (`database.py`)**: 
    *   Se crea el `engine` (motor) pasándole la `DATABASE_URL`.
    *   Se utiliza `sessionmaker` para crear instancias de `SessionLocal`, esto representa una "conversación" o una ventanilla de interacción exclusiva con la base.
3.  **Dependencia de Inyección (`get_db`)**: En el mismo `database.py`, hay una función `get_db()`. FastAPI la usa para dar y asegurar que cualquier ruta obtenga una sesión limpia hacia la base de datos, manteniéndola abierta durante la ejecución de la petición y finalmente cerrándola de forma segura en su cláusula `finally`.
4.  **Sincronización de Tablas (`main.py`)**: Con la orden `Base.metadata.create_all(bind=engine)`, se le instruye a la base de datos crear materialmente un reflejo de los modelos.

## 3. Explicación de `requirements.txt`

El archivo `requirements.txt` actúa como el "manifiesto" de las librerías o dependencias externas (no integradas en Python de manera nativa) que necesita tu aplicación y en qué versión las necesita, garantizando reproducibilidad.

En su interior vemos listadas:
*   `fastapi`, `uvicorn` (Para el servidor web de la API).
*   `sqlalchemy`, `psycopg2-binary` (Para funcionar y conectarse a PostgreSQL).
*   `pydantic`, `pydantic-settings`, `python-dotenv` (Para los esquemas y validación de variables de entorno).

Sirve principalmente para que cualquier desarrollador, o en este caso, un entorno de producción, instale todo de golpe asegurando las versiones compatibles empleando un solo comando:
```bash
pip install -r requirements.txt
```
