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


class Quiz(models.Model):
    document_id = models.IntegerField(unique=True)

    def get_quiz_questions(self):
        return QuizQuestion.objects.filter(quiz=self)


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.IntegerField(default=0)

    def get_quiz_answers(self):
        return QuizAnswer.objects.filter(question=self)


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
