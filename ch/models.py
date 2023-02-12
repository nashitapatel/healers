from django.db import models


class chathistory(models.Model):
    question=models.CharField(max_length=20)
    answer=models.CharField(max_length=100)
    conversation_time=models.DateTimeField()

# Create your models here.

