from django.contrib import admin

from .models import Media, ArObj, MediaType

# Register your models here.
admin.site.register(Media)
admin.site.register(ArObj)
admin.site.register(MediaType)
