from django.db import models

# Create your models here.

class register(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField()
    etc = models.TextField(blank=True, null=True)