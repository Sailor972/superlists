# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
ALLOWED_HOSTS = []
ADMINS = ()
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

from .settings_secret import *
