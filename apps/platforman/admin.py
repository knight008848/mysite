from django.contrib import admin
from .models import *

# Register your models here.


class platformAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'lob', 'product', 'phnum')
    ordering = ('name',)
    list_filter = ('lob', )


admin.site.register(Platform, platformAdmin)
