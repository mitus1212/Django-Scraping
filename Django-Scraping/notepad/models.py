from django.db import models
from django.conf import settings
from django.urls import reverse
from PIL import Image
# Create your models here.

class Note(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True, upload_to='notes')
    url = models.URLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notepad:note-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Note, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 600 or img.width > 600:
            output_size = (600,600)
            img.thumbnail(output_size)
            img.save(self.image.path)