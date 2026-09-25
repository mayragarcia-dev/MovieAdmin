from django.contrib import admin
from .models import Genre, Person, Movie, Rating


class RatingInline(admin.TabularInline):
    model = Rating
    extra = 0
    raw_id_fields = ('person',)
    readonly_fields = ('created_at',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'nationality')
    list_filter = ('nationality',)
    search_fields = ('name',)
    readonly_fields = ('created_at', 'updated_at')


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'duration')
    list_filter = ('genres', 'release_date')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'updated_at')
    inlines = [RatingInline]


class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'rating', 'person', 'created_at')
    list_filter = ('rating',)
    search_fields = ('movie__title',)
    readonly_fields = ('created_at',)


admin.site.register(Genre, GenreAdmin)
admin.site.register(Person, PersonAdmin)
admin.site.register(Movie, MovieAdmin)
admin.site.register(Rating, RatingAdmin)
