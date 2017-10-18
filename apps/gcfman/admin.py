from django.contrib import admin
from .models import *

# Register your models here.


class GcfAdmin(admin.ModelAdmin):
    list_display = ['number', 'level','model', 'family', 'ctomod', 'region', 'dest', 'add_time', 'OSV', 'OSP', 'OSD', 'siaccount', 'quantity']
    list_filter = ['family', 'OSV', 'level', 'ctomod']
    search_fields = ['po', 'family', 'mod', 'sdr']
    ordering = ('-add_time',)
    date_hierarchy = 'add_time'

    fieldsets = [
            ('Basic information', {
                'fields': (
                    ('number', 'level', 'family', 'model'),
                    ('dest', 'region', 'ctomod'),
                    ('OSV', 'OSP', 'OSD'),
                    'muiflag',
                    'cfiflag',
                    'siaccount',
                    'quantity'
                )
            }),
            ('Advanced information', {
                'fields': ('add_time', 'mod', 'sdr', 'filepath'),
                'classes': ('collapse',)
            })
                ]


admin.site.register(gcfnote, GcfAdmin)
