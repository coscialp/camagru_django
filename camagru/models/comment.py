from django.db import models
from ..models import Picture
from ..models import User


class Comment(models.Model):
    where = models.ForeignKey(Picture, on_delete=models.CASCADE)
    who = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=300, blank=False)
