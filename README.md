# CineAdmin 🎬

Proyecto Django 6.1 para la gestión y recomendación de películas.

## Objetivo del proyecto

Este proyecto tiene como objetivo demostrar las capacidades del panel de administración de Django (Django Admin) y la creación de vistas públicas personalizadas. Los puntos principales son:

1. **Modelado de datos**: Definir modelos con relaciones (muchos a muchos, claves foráneas)
2. **Django Admin personalizado**: Listas, filtros, búsqueda, formularios inline y campos de solo lectura
3. **Gestión de permisos**: Grupos con permisos limitados (crear y modificar, pero no eliminar)
4. **Vista pública**: Sistema de recomendación basado en valoraciones por género

## Tecnologías

- Python 3.14
- Django 6.1
- Pillow (imágenes)
- SQLite

## Estructura

```
MovieAdmin/
├── movieproject/          # Configuración del proyecto
├── movies/                # Aplicación principal
│   ├── models.py          # Movie, Genre, Person, Rating
│   ├── admin.py           # ModelAdmin personalizados
│   ├── views.py           # Vista de recomendaciones
│   ├── urls.py            # URLs públicas
│   ├── templates/movies/  # Plantillas HTML
│   └── management/commands/  # load_data.py
├── manage.py
└── db.sqlite3
```

## Instalación

```bash
pip install Django Pillow
python manage.py migrate
python manage.py load_data
python manage.py createsuperuser
python manage.py runserver
```

## Usuarios

| Usuario | Contraseña | Rol |
|---------|-----------|-----|
| admin | admin12345 | Superusuario (acceso total) |
| editor | editor12345 | Grupo "editores" (solo movies, sin eliminar) |

## Acceder

- **Admin**: http://127.0.0.1:8000/admin/
- **Recomendaciones**: http://127.0.0.1:8000/recommendations/
