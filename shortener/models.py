from django.db import models

# Create your models here.
class Url(models.Model):
    long_url = models.CharField(max_length=5000)
    uuid = models.CharField(max_length=15) 