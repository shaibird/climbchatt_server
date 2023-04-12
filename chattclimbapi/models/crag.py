from django.db import models

class Crag(models.Model):
    crag_name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.CharField(max_length=400)
    crag_type = models.ForeignKey("Crag", on_delete=models.CASCADE, related_name="crag_type")