from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=120)
    authors = models.CharField(max_length=120)
    date = models.DateField(blank=True)
    industryIdentifiers = models.CharField(max_length=240)

    pages = models.IntegerField()
    link = models.CharField(max_length=1024)
    language = models.CharField(max_length=64)

