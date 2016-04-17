# -*- coding: utf-8 -*-

import os

from django.core.cache import cache

from .conf import settings


class IPList(list):
    """Stolen from https://djangosnippets.org/snippets/1362/"""

    def __init__(self, ips):
        try:
            from IPy import IP
            for ip in ips:
                self.append(IP(ip))
        except ImportError:
            pass

    def __contains__(self, ip):
        try:
            for net in self:
                if ip in net:
                    return True
        except:
            pass
        return False


def activate():
    cache.add(settings.MAINTENANCE_LOCK_KEY, '1', timeout=None)


def deactivate():
    cache.delete(settings.MAINTENANCE_LOCK_KEY)


def status():
    return settings.MAINTENANCE_MODE or cache.get(settings.MAINTENANCE_LOCK_KEY)
