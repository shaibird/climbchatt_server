from django.db import models

class Climb(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    crag = models.ForeignKey("Crag", on_delete=models.CASCADE, related_name="climbs_crag")
    style = models.ForeignKey("Style", on_delete=models.CASCADE, related_name="climbs_style")
    grade = models.ForeignKey("Grade", on_delete=models.CASCADE, related_name="climbs_grade")
    user_climbed = models.BooleanField(default=False)
    user_ticked = models.BooleanField(default=False)