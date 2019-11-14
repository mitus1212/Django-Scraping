from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('rest_books',BookView.as_view(), name="rest_books"),
    ]



urlpatterns = format_suffix_patterns(urlpatterns)
