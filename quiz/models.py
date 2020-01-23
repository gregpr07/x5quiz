from django.contrib.auth.models import User
from django.db import models


class ResourceStatistics(models.Model):
    resource_id = models.IntegerField(unique=True)
    rating = models.FloatField(default=5)
    raters = models.ManyToManyField(User)
    views = models.IntegerField(default=0)

    def __str__(self):
        return str(self.resource_id) + "'s statistics"
