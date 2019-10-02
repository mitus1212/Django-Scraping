  GNU nano 2.9.8                                                                                         urls.py                                                                                                   
"""dashboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from news.views import scrape, scrape_weather
from finance.views import company_article_list, ChartData
from django.conf import settings
from django.conf.urls.static import static
from charts.views import chart_view

urlpatterns = [
    path('chart/', chart_view, name='chart'),
    path('notes/', include('notepad.urls', namespace='notes')),
    path('admin/', admin.site.urls),
    path('scrape/', scrape, name='scrape'),
    path('weather/', scrape_weather, name='weather'),
    path('companies/', company_article_list, name='companies'),
    path('', include('news.urls')),
    path('', include('notepad.urls')),
    path('api/chart/data/',ChartData.as_view(), name='api_chart-data'),


]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



