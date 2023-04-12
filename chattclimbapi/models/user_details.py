from django.db import models
from django.contrib.auth.models import User

class UserDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_details")
    ape_index = models.FloatField()
    birthday = models.DateField()
    height = models.FloatField()