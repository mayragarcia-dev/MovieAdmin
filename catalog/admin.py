from django.contrib import admin
from .models import Genre, Movie, Rating


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0
    readonly_fields = ['user', 'score', 'created_at']
    can_delete = False

    def has_add_permission(self, request, obj=None):
        return False


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']
    search_fields = ['name']
    list_filter = ['created_at']


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'release_date', 'duration', 'created_at']
    list_filter = ['genre', 'release_date', 'created_at']
    search_fields = ['title', 'description']
    readonly_fields = ['created_at', 'updated_at']
    inlines = [RatingInline]
    date_hierarchy = 'created_at'


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ['movie', 'user', 'score', 'created_at']
    list_filter = ['score', 'created_at']
    search_fields = ['movie__title', 'user__username']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
