# Portal de Noticias - Django

Proyecto de portal de noticias desarrollado con Django.

## Características

- App `news` con modelos: Article, Category, Author
- Plantillas base con herencia (`base.html`)
- Tarjeta de artículo reutilizable (`_article_card.html`)
- Portada con listado de noticias y paginación
- Listado por categorías
- Configuración de archivos estáticos y multimedia
- Panel de administración Django

## Modelos

### Category
- name: Nombre de la categoría
- slug: URL amigable
- created_at, updated_at: Fechas de auditoría

### Author
- user: Relación OneToOne con User de Django
- bio: Biografía
- avatar: Imagen de perfil
- created_at, updated_at: Fechas de auditoría

### Article
- title: Título del artículo
- slug: URL amigable
- summary: Resumen breve
- content: Contenido completo
- featured_image: Imagen destacada
- published_at: Fecha de publicación
- updated_at: Fecha de actualización
- is_published: Estado de publicación
- category: ForeignKey a Category
- author: ForeignKey a Author

## Instalación

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Superusuario

- Usuario: admin
- Contraseña: admin123