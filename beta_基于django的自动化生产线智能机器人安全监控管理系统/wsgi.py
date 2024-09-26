"""
WSGI config for beta_基于django的自动化生产线智能机器人安全监控管理系统 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "beta_基于django的自动化生产线智能机器人安全监控管理系统.settings",
)

application = get_wsgi_application()
