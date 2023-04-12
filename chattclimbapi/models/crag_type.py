from django.db import models

class CragType(models.Model):
    type = models.CharField(max_length=100)