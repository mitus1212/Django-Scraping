from django.db import models
from django.conf import settings

# Create your models here.

class Headline(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    url = models.TextField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    last_scrape = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return "{}-{}".format(self.user,self.last_scrape)

class Weather(models.Model):
    weather = models.TextField()
    degree = models.CharField(max_length=200)
    pressure = models.IntegerField()