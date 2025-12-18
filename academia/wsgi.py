"""
WSGI config for academia project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "academia.settings")


# para hacer deploy en vercel -> documentacion: https://vercel.com/templates/backend/django-hello-world
# application = get_wsgi_application()
app = get_wsgi_application()