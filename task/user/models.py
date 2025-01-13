from django.db import models
from django.contrib.auth import get_user_model


class App(models.Model):
    name = models.CharField(max_length=255)
    points = models.IntegerField()

class Task(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')