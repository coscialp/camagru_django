from django.db import models
from ..models import Picture
from ..models import User


class Dislike(models.Model):
    where = models.ForeignKey(Picture, on_delete=models.CASCADE)
    who = models.ForeignKey(User, on_delete=models.CASCADE)
