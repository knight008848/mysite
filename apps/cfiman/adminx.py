# -*- coding:utf-8 -*-

import xadmin

from .models import *


class CfiAdmin(object):
    list_display = ['account', 'add_time', 'last_modify', 'size']
    search_fields = ['account']
    ordering = ('-last_modify',)
    date_hierarchy = 'add_time'


class PatchAdmin(object):
    list_display = ['number', 'add_time', 'is_active']
    search_fields = ['number']
    ordering = ('-add_time',)
    date_hierarchy = 'add_time'


xadmin.site.register(cfinote, CfiAdmin)
# xadmin.site.register(patch, PatchAdmin)
