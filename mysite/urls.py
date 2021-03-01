from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('lightbulbs/', views.LightbulbView, name='lightbulb'),
    path('blinds/', views.BlindsView, name='blinds'),
    path('temperature/', views.TemperatureView, name='temperature'),
]