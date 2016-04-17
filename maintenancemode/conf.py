# -*- coding: utf-8 -*-

import os

from django.conf import settings  # pylint: disable=W0611
from appconf import AppConf


class MaintenanceSettings(AppConf):
    IGNORE_URLS = ()
    LOCK_KEY = 'maintenance.lock'
    MODE = False

    class Meta:
        prefix = 'maintenance'
        holder = 'maintenancemode.conf.settings'
