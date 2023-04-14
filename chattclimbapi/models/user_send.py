from django.db import models
from django.contrib.auth.models import User


class UserSend(models.Model):
    climb = models.ForeignKey("Climb", on_delete=models.CASCADE, related_name="sent_climbs")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_send")
    comment = models.CharField(max_length=(1000))
    date = models.DateTimeField(auto_now_add=True)
    steep = models.ForeignKey("Steep", on_delete=models.CASCADE, related_name="climb_steep")
    hold_type = models.ForeignKey("HoldType", on_delete=models.CASCADE, related_name="climb_hold_type")
    rating = models.ForeignKey("Rating",on_delete=models.CASCADE, related_name="climb_rating" )
    grade = models.ForeignKey("Grade", on_delete=models.CASCADE, related_name="climb_grade")
