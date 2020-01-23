from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='quiz-index'),
    path('search/<str:query>/', views.search_view, name='quiz-index'),
    path('learn/<str:document_id>/', views.learn_view, name='quiz-learn'),
]