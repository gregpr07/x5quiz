from django.contrib.auth.models import User
from django.db import models


class DocumentStatistics(models.Model):
    document_id = models.IntegerField(unique=True)
    rating = models.FloatField(default=5)
    raters = models.ManyToManyField(User)
    views = models.IntegerField(default=0)

    def __str__(self):
        return str(self.document_id) + "'s statistics"

    def increase_views(self):
        self.views = self.views + 1
        self.save()
