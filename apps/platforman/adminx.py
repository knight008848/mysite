# -*- coding:utf-8 -*-

import xadmin

from .models import *


class platformAdmin(object):
    list_display = ['name', 'model', 'lob', 'product', 'phnum']
    search_fields = ('name',)
    ordering = ('name',)
    list_filter = ['lob']


xadmin.site.register(Platform, platformAdmin)
