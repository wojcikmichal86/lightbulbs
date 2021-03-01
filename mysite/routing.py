from django.urls import path
from .consumers import DeviceConsumer, BlindsConsumer, TemperatureConsumer

ws_urlpatterns = [
    path('ws/lightbulbs/', DeviceConsumer.as_asgi()),
    path('ws/blinds/', BlindsConsumer.as_asgi()),
    path('ws/temperature/', TemperatureConsumer.as_asgi())
]
