from django.urls import path
from . import views

app_name = 'weather_api'
urlpatterns = [
    path('', views.index, name='index'),
    path('get_weather/', views.get_weather, name='get_weather'),
]