from django.urls import path
from .views import news_list, weather_remove


app_name = 'news'


urlpatterns = [
    path('home/', news_list, name='home'),
    path('remove/<int:pk>/', weather_remove, name='remove'),

]
