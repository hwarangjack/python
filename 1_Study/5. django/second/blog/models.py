from django.db import models

# Create your models here.

class post(models.Model):
    who = models.CharField(max_length=30)
    text = models.TextField()
    picture = models.FileField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.who