from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.title