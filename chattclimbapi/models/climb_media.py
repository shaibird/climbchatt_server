from django.db import models

class ClimbMedia(models.Model):
    video = models.FileField(upload_to='videos/')
    climb = models.ForeignKey("Climb", on_delete=models.CASCADE, related_name="climb_videos")