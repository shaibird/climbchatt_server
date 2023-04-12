from django.db import models

class Steep(models.Model):
    steep = models.CharField(max_length=(50))
    