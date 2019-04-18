from django.urls import path
from .views import create_view, list_view, delete_view, NoteDetailView
app_name = 'notepad'

urlpatterns = [
    path('create/', create_view, name='create'),
    path('list/', list_view, name='list'),
    path('<id>/delete/', delete_view, name='delete'),
    path('note/<int:pk>', NoteDetailView.as_view(), name='note_detail'),




]
