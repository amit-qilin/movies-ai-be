from django.contrib import admin
from .models import Movie

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'release_date', 'rating', 'genre')
    list_filter = ('genre', 'release_date', 'rating')
    search_fields = ('title', 'director', 'description')
    date_hierarchy = 'release_date'
    ordering = ('-release_date',)
