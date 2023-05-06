from django.db import models
from django.contrib.auth.models import User

class Crag(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, default="")
    latitude = models.FloatField()
    longitude = models.FloatField()
    state = models.ForeignKey("State", on_delete=models.DO_NOTHING, related_name="crag_state", default="")
    country = models.ForeignKey("Country", on_delete=models.DO_NOTHING, related_name="crag_country", default="")
    description = models.CharField(max_length=400)
    type = models.ForeignKey("Crag", on_delete=models.CASCADE, related_name="crag_type")
    access = models.CharField(max_length=500, null=True, default="")
    private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_crags", default="")