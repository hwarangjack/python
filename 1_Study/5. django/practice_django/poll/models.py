from django.db import models

# Create your models here.
class question(models.Model):
    question_text = models.CharField(max_length=20)
    pub_date = models.DateField('date published')

    def __str__(self):
        return self.question_text

class choice(models.Model):
    question = models.ForeignKey(question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text