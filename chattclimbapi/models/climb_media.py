from django.db import models

class ClimbMedia(models.Model):
    video = models.FileField(null=True, blank=True, upload_to='videos/')
    image = models.ImageField(null=True, blank=True, height_field=None,
                              width_field=None, max_length=None, upload_to="images")
    climb = models.ForeignKey("Climb", on_delete=models.CASCADE, related_name="climb_videos")
