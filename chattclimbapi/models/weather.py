from django.db import models
from django.contrib.auth.models import User

class Weather(models.Model):
    conditions = models.CharField(max_length=100)