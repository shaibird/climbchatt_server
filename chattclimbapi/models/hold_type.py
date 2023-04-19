from django.db import models

class HoldType(models.Model):
    type = models.CharField(null=True, blank=True, max_length=70)