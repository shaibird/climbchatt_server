from django.db import models

class Climb(models.Model):
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    crag = models.ForeignKey("Crag", on_delete=models.CASCADE, related_name="climbs_crag")
    steep = models.ForeignKey("Steep", on_delete=models.CASCADE, related_name="climbs_steep", default=False)
    grade = models.ForeignKey("Grade", on_delete=models.CASCADE, related_name="climbs_grade")
    hold_type = models.ForeignKey("HoldType", on_delete=models.CASCADE, related_name="climbs_holds", default=False)
    user_climbed = models.BooleanField(default=False)
    user_ticked = models.BooleanField(default=False)