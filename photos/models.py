from django.db import models

# Create your models here.
class Photos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.FilePathField(path="/img")