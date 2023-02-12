from django.db import models

# Create your models here.
class QnA(models.Model):
    question=models.CharField(max_length=40)
    answer=models.CharField(max_length=40)