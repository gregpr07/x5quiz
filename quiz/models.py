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

    def get_quiz_question(self, index):
        return QuizQuestion.objects.filter(quiz=self)[index]


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    correct = models.IntegerField(default=0)

    def get_quiz_answers(self):
        return QuizAnswer.objects.filter(question=self)


class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)


class QuizUserResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    correct = models.IntegerField(default=0)
    wrong = models.IntegerField(default=0)
    data = models.TextField(max_length=500)

    def get_correct_percentage(self):
        return (self.correct * 100) / (self.correct + self.wrong)

    def get_wrong_percentage(self):
        return (self.wrong * 100) / (self.correct + self.wrong)

    def determine_grade(self):
        correct_percentage = self.get_correct_percentage()
        if correct_percentage >= 90: return 'A'
        if correct_percentage >= 80: return 'B'
        if correct_percentage >= 70: return 'C'
        if correct_percentage >= 60: return 'D'
        if correct_percentage >= 50: return 'E'
        return 'F'

