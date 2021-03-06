# -*- coding:utf-8 -*- 

import xadmin

from .models import *


class GcfAdmin(object):
    list_display = ['number', 'level','model', 'family', 'ctomod', 'region', 'dest', 'add_time', 'OSV', 'OSP', 'OSD', 'siaccount', 'quantity']
    list_filter = ['family', 'OSV', 'level', 'ctomod']
    search_fields = ['po', 'family', 'mod', 'sdr']
    ordering = ('-add_time',)
    date_hierarchy = 'add_time'


xadmin.site.register(gcfnote, GcfAdmin)
