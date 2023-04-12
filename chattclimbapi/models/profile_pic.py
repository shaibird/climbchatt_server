from django.db import models
from django.contrib.auth.models import User

class ProfilePic(models.Model):
    image = models.ImageField(null=True, blank=True, height_field=None, width_field=None, max_length=None, upload_to="images")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile_picture")