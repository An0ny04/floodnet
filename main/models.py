from django.db import models

# Create your models here.
class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    count = models.IntegerField(null=True, blank=True)