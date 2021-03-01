from django.urls import include, path
from . import views



urlpatterns = [
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('lightbulbs/', views.LightbulbList, name='lightbulbs'),
    path('lightbulbs/detail/<str:pk>', views.LightbulbDetail, name='lightbulbdetail'),
    path('lightbulbs/create', views.LightbulbCreate, name='lightbulbcreate'),
    path('lightbulbs/update/<str:pk>', views.LightbulbUpdate, name='lightbulbupdate'),
    path('lightbulbs/delete/<str:pk>', views.LightbulbDelete, name='lightbulbdelete'),
    path('blinds/', views.BlindsList, name='blindsdevices'),
    path('blinds/detail/<str:pk>', views.BlindsDetail, name='blindsdetail'),
    path('blinds/create', views.BlindsCreate, name='blindscreate'),
    path('blinds/update/<str:pk>', views.BlindsUpdate, name='blindsupdate'),
    path('blinds/delete/<str:pk>', views.BlindsDelete, name='blindsdelete'),
    path('temperature/', views.TemperatureList, name='temperaturedevices'),
    path('temperature/detail/<str:pk>', views.TemperatureDetail, name='temperaturedetail'),
    path('temperature/create', views.TemperatureCreate, name='temperaturecreate'),
    path('temperature/update/<str:pk>', views.TemperatureUpdate, name='temperatureupdate'),
    path('temperature/delete/<str:pk>', views.TemperatureDelete, name='temperaturedelete'),
]
