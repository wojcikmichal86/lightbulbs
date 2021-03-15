"""
ASGI config for django_api project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter, URLRouter #required for adding websocket protocol
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
from mysite.routing import ws_urlpatterns #adds the websocket urls to the protocol router

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_api.settings')

application = ProtocolTypeRouter({
    'http':get_asgi_application(),
    'websocket': AuthMiddlewareStack(URLRouter(ws_urlpatterns)),
})

