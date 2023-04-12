from django.db import models

class CragImage(models.Model):
    image = models.ImageField(null=True, blank=True, height_field=None,
                              width_field=None, max_length=None, upload_to="images")
    crag = models.ForeignKey("Crag", on_delete=models.CASCADE)