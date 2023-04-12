from django.db import models

class HoldType(models.Model):
    type = models.CharField(max_length=(70))