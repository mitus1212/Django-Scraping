from django.contrib import admin
from .models import Headline, UserProfile, Weather
# Register your models here.
admin.site.register(Headline)
admin.site.register(UserProfile)
admin.site.register(Weather)