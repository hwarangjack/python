from django.db import models

# Create your models here.

class post(models.Model):
    who = models.CharField(max_length=30)
    text = models.TextField()
    # picture = models.ImageField()
    date = models.DateTimeField()
