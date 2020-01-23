from django.urls import path

from . import views

urlpatterns = [
    path('profile/<str:username>/', views.profile_view, name='accounts-profile'),
    path('members/', views.members_view, name='accounts-members'),
    path('login/', views.login_view, name='accounts-login'),
    path('signup/', views.signup_view, name='accounts-signup'),
    path('home/', views.home_view, name='accounts-home'),
    path('logout/', views.logout_view, name='accounts-logout'),
]