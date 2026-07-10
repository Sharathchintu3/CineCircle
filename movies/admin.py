from django.contrib import admin
from .models import Movie, Genre
# Register your models here.
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    last_display = ("name", "tmdb_id")
    search_fields = ("name", )

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "release_date",
        "vote_average",
        "popularity",
    )
    search_fields = ("title",)
    list_filter = (
        "original_language",
        "genres",
    )