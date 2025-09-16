# Sistema de Inventario (Flask + SQLite)


### 1) Requisitos
- Python 3.10+


### 2) Instalación
```bash
python -m venv .venv
# Windows
.venv\\Scripts\\activate
# macOS / Linux
source .venv/bin/activate


pip install -r requirements.txt
```


### 3) Variables de entorno (opcional)
Crea un archivo `.env` (opcional):
```
FLASK_DEBUG=1
FLASK_SECRET=supersecretok
DATABASE_URL=sqlite:///inventario.db
```


### 4) Inicializar BD y ejecutar
```bash
# Inicializa tablas\python app.py --init-db


# Ejecuta servidor
python app.py
# visita: http://127.0.0.1:5000/
```


> Usuario/clave no requeridos (demo). Para uso real, agrega autenticación.
```