from django.db import models


class Picture(models.Model):
    title = models.CharField(max_length=100, blank=True)
    img = models.ImageField(upload_to="img/profile_pictures", blank=False)
