from django.db import models
from django.contrib.auth.models import User

class UserTick(models.Model):
    climb = models.ForeignKey("Climb", on_delete=models.CASCADE, related_name="climb_comments")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_comments")