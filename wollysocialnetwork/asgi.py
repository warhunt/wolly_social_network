"""
ASGI config for wollysocialnetwork project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
import django

from django.core.asgi import get_asgi_application


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wollysocialnetwork.settings')
django_app = get_asgi_application()

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

import main.routing

application = ProtocolTypeRouter({
  "https": django_app,
  "websocket": AuthMiddlewareStack(
    URLRouter(
        main.routing.websocket_urlpatterns
    )
  )
})
