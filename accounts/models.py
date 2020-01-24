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
    points = models.IntegerField(default=0)

    def add_points(self, amount):
        self.points = self.points + amount
        self.save()

    def increase_documents_read(self):
        self.documents_read = self.documents_read + 1
        self.save()

    def increase_quizzes_played(self):
        self.quizzes_played = self.quizzes_played + 1
        self.save()

    def __str__(self):
        return self.user.username + "'s statistics"
