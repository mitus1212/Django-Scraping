from django.urls import path
from .views import create_view, list_view, delete_view
app_name = 'notepad'

urlpatterns = [
    path('create/', create_view, name='create'),
    path('list/', list_view, name='list'),
    path('<id>/delete/', delete_view, name='delete'),


]
