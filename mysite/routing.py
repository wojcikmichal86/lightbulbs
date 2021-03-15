from django.urls import path
from .consumers import LightbulbConsumer, BlindsConsumer, TemperatureConsumer

ws_urlpatterns = [
    path('ws/lightbulbs/', LightbulbConsumer.as_asgi()), #routes the view for the LightbulbWebsocket path to its consumer
    path('ws/blinds/', BlindsConsumer.as_asgi()), #routes the view for the BlindsWebsocket path to its consumer
    path('ws/temperature/', TemperatureConsumer.as_asgi()) #routes the view for the TemperatureWebsocket path to its consumer
]
