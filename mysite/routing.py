from django.urls import path
from .consumers import LightbulbConsumer, BlindsConsumer, TemperatureConsumer

ws_urlpatterns = [
    path('ws/lightbulbs/', LightbulbConsumer.as_asgi()), #provides the view for the LightbulbWebsocket path
    path('ws/blinds/', BlindsConsumer.as_asgi()), #provides the view for the BlindsWebsocket path
    path('ws/temperature/', TemperatureConsumer.as_asgi()) #provides the view for the TemperatureWebsocket path
]
