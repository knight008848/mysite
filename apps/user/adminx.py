# -*- coding:utf-8 -*-

import xadmin
from xadmin import views


class GlobalSetting(object):
    site_title = '软件后台管理系统'
    site_footer = 'Pegatron SW5'


xadmin.site.register(views.CommAdminView, GlobalSetting)
