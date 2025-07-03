"""
WSGI config for Law_firm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Law_firm.settings')

import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Law_firm.settings')

# 👇👇 AUTO RUN MIGRATIONS
django.setup()
from django.core.management import call_command
try:
    call_command('migrate', interactive=False)
except Exception as e:
    print("Migration error:", e)

application = get_wsgi_application()


application = get_wsgi_application()


