from django.db import models

# Create your models here.

class Alias(models.Model):
    short_url =models.CharField(max_length=8)
    original_url = models.TextField()
