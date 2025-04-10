# crud_project

Proyecto escalable para la gestión de productos utilizando Django como frontend (UI + ORM) y FastAPI para la API REST. Actualmente, el proyecto se encuentra en una fase inicial con funcionalidades básicas de CRUD en Django y un endpoint simple en FastAPI.

---

## Estructura del proyecto
crud_project/
│
├── backend/                        # Proyecto Django (UI + ORM)
│   ├── config/                    # Configuración principal del proyecto Django
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   │
│   ├── products/                  # App de Django con el CRUD de productos
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   └── products/
│   │   │       └── list.html     # Vista para mostrar los productos
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   │
│   ├── manage.py
│
├── api/                            # Proyecto FastAPI
│   ├── main.py                    # Punto de entrada para FastAPI
│   └── routes/                    # (A crear) Rutas futuras para la API REST
│
├── requirements.txt               # Archivo de dependencias
├── .env                           # Variables de entorno (para cuando uses PostgreSQL)
├── venv/                          # Entorno virtual (no se sube al repo)
└── README.md                      # 📍 Archivo README, va en el nivel raíz

---

## 🚀 Tecnologías utilizadas

- **Python 3.11+**
- **Django** (Frontend + ORM)
- **FastAPI** (API REST)
- **SQLite** (temporalmente para pruebas locales)
- **HTML (Templates de Django)**

---

## ✅ Funcionalidades actuales

- CRUD de productos con:
  - Nombre
  - Descripción
  - Precio
  - Stock
- UI básica en Django
- Endpoint `/ping` en FastAPI para pruebas

---

## ▶️ Instrucciones de uso (modo local)

1. Clona el repositorio

```bash
git clone https://github.com/Jeff-Deck/Web1.git
cd crud_project

2. Crea y activa un entorno virtual

python -m venv venv
.\venv\Scripts\activate   # Windows

3. Instala las dependencias

pip install -r requirements.txt

4. Ejecuta el servidor Django
cd backend
python manage.py migrate
python manage.py runserver

5. Ejecuta FastAPI (en otra terminal)
cd api
uvicorn main:app --reload --port 8001

