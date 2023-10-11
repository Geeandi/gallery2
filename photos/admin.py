from django.contrib import admin
from .models import Photo, Album

# Register your models here.

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'album', 'date')
    ordering = ('date', )
    search_fields = ('name', )

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'date', 'description')
    ordering = ('name', )
    search_fields = ('name', )
