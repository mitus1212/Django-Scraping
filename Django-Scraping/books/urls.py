from django.urls import path, include
from . import views
from rest_framework import routers
from .views import BookView, csv_exporter
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('rest_books',BookView.as_view(), name="rest_books"),
    path('csv', csv_exporter, name='csv_exporter'),

    ]

urlpatterns = format_suffix_patterns(urlpatterns)
