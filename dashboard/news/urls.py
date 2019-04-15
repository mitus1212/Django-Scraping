from django.urls import path
from .views import news_list, weather_remove, article_remove


app_name = 'news'


urlpatterns = [
    path('home/', news_list, name='home'),
    path('remove_weather/<int:pk>/', weather_remove, name='weather_remove'),
    path('remove_news/<int:pk>/', article_remove, name='article_remove'),

]
