"""
ASGI config for hrm project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application  # pylint: disable=E0611 disable=E0401


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hrm.settings')

application = get_asgi_application()
