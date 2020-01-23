from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300, default="Another cool user.")
    avatar = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.user.username + "'s profile"


class ProfileStatistics(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documents_read = models.IntegerField(default=0)
    documents_rated = models.IntegerField(default=0)
    quizzes_played = models.IntegerField(default=0)
