from django.contrib import admin

from photos.models import Photos


# Register your models here.
class PhotosAdminModels(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'album', 'private', 'create_date']
    list_display_links = ['id', 'title']
    search_fields = ['title']
    fields = ['title', 'photo', 'author', 'album', 'private']


admin.site.register(Photos, PhotosAdminModels)