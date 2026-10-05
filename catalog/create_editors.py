import os
import sys
import django

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import Group, Permission
from catalog.models import Movie, Genre, Rating

# Crear grupo "Editores"
editors_group, created = Group.objects.get_or_create(name='Editores')
print(f"Grupo 'Editores': {'creado' if created else 'ya existía'}")

# Permisos para el grupo Editores (solo CRUD básico)
# Movies: add, change, delete, view
editors_group.permissions.set([
    Permission.objects.get(codename='add_movie'),
    Permission.objects.get(codename='change_movie'),
    Permission.objects.get(codename='delete_movie'),
    Permission.objects.get(codename='view_movie'),
    Permission.objects.get(codename='add_genre'),
    Permission.objects.get(codename='change_genre'),
    Permission.objects.get(codename='delete_genre'),
    Permission.objects.get(codename='view_genre'),
    Permission.objects.get(codename='add_rating'),
    Permission.objects.get(codename='change_rating'),
    Permission.objects.get(codename='delete_rating'),
    Permission.objects.get(codename='view_rating'),
])
print("Permisos asignados al grupo 'Editores'")

# Crear usuario editor
from django.contrib.auth.models import User
editor_user, created = User.objects.get_or_create(
    username='editor',
    defaults={
        'email': 'editor@example.com',
        'is_staff': True,
    }
)
editor_user.set_password('Editor123!')
editor_user.save()
editor_user.groups.add(editors_group)
print(f"Usuario editor: {'creado' if created else 'ya existía'} - editor / Editor123!")

print("\nResumen de diferencias:")
print("  Superusuario (admin): acceso TOTAL a todo el admin")
print("  Usuario editor: acceso SOLO al catálogo (peliculas, generos, valoraciones) NO puede crear usuarios ni grupos")
