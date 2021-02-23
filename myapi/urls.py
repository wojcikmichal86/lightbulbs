from django.urls import include, path
from . import views



urlpatterns = [
    path('', views.deviceList, name='devices'),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('detail/<str:pk>', views.deviceDetail, name='detail'),
    path('create', views.deviceCreate, name='create'),
    path('update/<str:pk>', views.deviceUpdate, name='update'),
    path('delete/<str:pk>', views.deviceDelete, name='delete'),
]
