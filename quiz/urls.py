from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='quiz-index'),
    path('search/', views.search_view, name='quiz-search'),
    path('learn/<str:document_id>/', views.learn_view, name='quiz-learn'),
    path('quiz/<str:document_id>/', views.quiz_view, name='quiz-quiz'),
    path('results/', views.results_view, name='quiz-results'),
    path('quiz-submit/<int:quiz_pk>', views.quiz_submit_view, name='quiz-submit'),
]