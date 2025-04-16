# crud_project

Proyecto escalable para la gestión de productos utilizando Django como frontend (UI + ORM) y FastAPI para la API REST. Actualmente, el proyecto cuenta con un CRUD funcional de productos, sistema de autenticación con login/logout, y una interfaz básica con navegación dinámica. FastAPI se encuentra integrado con un endpoint inicial y quedará disponible para desarrollos posteriores.

---

## 🗂 Estructura del proyecto
```
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
│   │   │       ├── base.html         # Template base con header dinámico
│   │   │       ├── home.html         # Página principal
│   │   │       ├── list.html         # Listado de productos
│   │   │       ├── form.html         # Crear/editar productos
│   │   │       ├── login.html        # Formulario de inicio de sesión
│   │   │       └── confirm_delete.html  # Confirmación para eliminar
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   │
│   └── manage.py
│
├── api/                            # Proyecto FastAPI
│   ├── main.py                    # Punto de entrada para FastAPI
│   └── routes/                    # (A crear) Rutas futuras para la API REST
│
├── requirements.txt               # Archivo de dependencias
├── .env                           # Variables de entorno (para cuando uses PostgreSQL)
├── venv/                          # Entorno virtual (no se sube al repo)
└── README.md                      # 📍 Este archivo
```

---

## 🚀 Tecnologías utilizadas

- **Python 3.11+**
- **Django 5.2** (Frontend + ORM)
- **FastAPI** (API REST - opcional por ahora)
- **SQLite** (desarrollo local)
- **Tailwind CSS** (UI limpia y moderna)
- **HTML + Django Templates**
- **django-widget-tweaks** (para personalizar formularios)

---

## ✅ Funcionalidades actuales

- CRUD de productos:
  - Nombre, descripción, precio, stock
- Sistema de login/logout
- Acceso restringido a funcionalidades CRUD
- Barra de navegación dinámica:
  - `Home`, `Products`, `Admin`, `Login`, `Logout`
  - Botones visibles según si el usuario está autenticado
- Endpoint `/ping` de prueba con FastAPI

---

## ▶️ Instrucciones de uso (modo local)

1. **Clona el repositorio**
```bash
git clone https://github.com/Jeff-Deck/Web1.git
cd crud_project
```

2. **Crea y activa un entorno virtual**
```bash
python -m venv venv
.env\Scriptsctivate   # En Windows
```

3. **Instala las dependencias**
```bash
pip install -r requirements.txt
```

4. **Ejecuta el servidor Django**
```bash
cd backend
python manage.py migrate
python manage.py runserver
```

5. **(Opcional) Ejecuta FastAPI en otra terminal**
```bash
cd api
uvicorn main:app --reload --port 8001
```

---

## 📌 Notas

- Puedes crear un superusuario con:
```bash
python manage.py createsuperuser
```

- Accede al panel de administración en: `http://127.0.0.1:8000/admin/`

- A futuro se integrará PostgreSQL con Docker y se activará la API REST completa con FastAPI.

---
