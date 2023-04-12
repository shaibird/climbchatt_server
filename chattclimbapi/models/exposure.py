from django.db import models

class Exposure(models.Model):
    type = models.CharField(max_length=50)