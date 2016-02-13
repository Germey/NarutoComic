from django.contrib import admin

# Register your models here.
from .models import Content, Image


class ContentAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')


class ImageAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'page')


admin.site.register(Content, ContentAdmin)
admin.site.register(Image, ImageAdmin)