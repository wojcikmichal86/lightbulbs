from django.urls import path
from .consumers import DeviceConsumer

ws_urlpatterns = [
    path('ws/lightbulbs/', DeviceConsumer.as_asgi())
]
