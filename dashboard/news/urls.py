from django.urls import path
from .views import news_list


app_name = 'news'


urlpatterns = [
    path('home/', news_list, name='home'),

]
