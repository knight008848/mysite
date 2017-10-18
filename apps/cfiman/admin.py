from django.contrib import admin
from .models import *

# Register your models here.


class CfiAdmin(admin.ModelAdmin):
    list_display = ['account', 'add_time', 'last_modify', 'size']
    search_fields = ['account']
    ordering = ('-last_modify',)
    date_hierarchy = 'add_time'


class PatchAdmin(admin.ModelAdmin):
    list_display = ['number', 'add_time', 'is_active']
    search_fields = ['number']
    ordering = ('-add_time',)
    date_hierarchy = 'add_time'


admin.site.register(cfinote, CfiAdmin)
# admin.site.register(patch, PatchAdmin)
