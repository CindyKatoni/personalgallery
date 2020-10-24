from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Photos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('image')
    