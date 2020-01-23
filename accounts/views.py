from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import LoginForm, SignupForm
from accounts.models import Profile
from x5quiz.errors import already_authenticated, not_authenticated


def login_view(request):
    if request.user.is_authenticated:
        return already_authenticated(request)

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if not form.is_valid():
            return render(request, 'accounts/login.html', {'form': form})

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        user = authenticate(request, username=username, password=password)

        if user is None:
            form.add_error('password', "Wrong username or password!")
            return render(request, 'accounts/login.html', {'form': form})

        login(request, user)
        return redirect('accounts-home')
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def signup_view(request):
    if request.user.is_authenticated:
        return already_authenticated(request)

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if not form.is_valid():
            return render(request, 'accounts/signup.html', {'form': form})

        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        confirm_password = form.cleaned_data['confirm_password']

        if password != confirm_password:
            form.add_error('confirm_password', "Passwords do not match!")
            return render(request, 'accounts/signup.html', {'form': form})

        if User.objects.filter(username=username).exists():
            form.add_error('username', "User with this username already exists.")
            return render(request, 'accounts/signup.html', {'form': form})

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        profile = Profile.objects.create(user=user, avatar="images/user-fallback.png")
        profile.save()

        login(request, user)

        return redirect('accounts-profile', username=request.user.username)
    else:
        form = SignupForm()
        return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    if not request.user.is_authenticated:
        return not_authenticated(request)

    logout(request)
    return render(request, 'accounts/logout.html', {})


def home_view(request):
    return render(request, "accounts/home.html", {})


def profile_view(request, username):
    return render(request, "accounts/profile.html", {})

