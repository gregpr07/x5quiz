from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='quiz-index'),
    path('search/<str:keyword>/', views.search_view, name='quiz-index'),
]