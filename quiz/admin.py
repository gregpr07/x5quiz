from django.contrib import admin

from quiz.models import DocumentStatistics, Quiz, QuizQuestion, QuizAnswer, QuizUserResult

admin.site.register(DocumentStatistics)
admin.site.register(Quiz)
admin.site.register(QuizQuestion)
admin.site.register(QuizAnswer)
admin.site.register(QuizUserResult)
