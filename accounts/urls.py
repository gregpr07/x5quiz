from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login_view, name='accounts-login'),
    path('signup/', views.login_view, name='accounts-signup'),
    path('home/', views.login_view, name='accounts-home'),
]