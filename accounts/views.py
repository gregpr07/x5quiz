from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from accounts.forms import LoginForm, SignupForm, SettingsForm
from accounts.models import Profile, ProfileStatistics
from quiz.models import QuizUserResult
from x5quiz.errors import already_authenticated, not_authenticated, unknown_user


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

        statistics = ProfileStatistics.objects.create(user=user)
        statistics.save()

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
    if not request.user.is_authenticated:
        return not_authenticated(request)

    return render(request, "accounts/home.html", {'recent': QuizUserResult.objects.filter(user=request.user)})


def profile_view(request, username):
    if not User.objects.filter(username=username).exists():
        return unknown_user(request)

    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)
    statistics = ProfileStatistics.objects.get(user=user)

    return render(request, "accounts/profile.html", {
        'user': user,
        'profile': profile,
        'statistics': statistics,
    })


def members_view(request):
    return render(request, "accounts/members.html", {
        'members': User.objects.all().order_by("-profilestatistics__points")
    })


def settings_view(request):
    if not request.user.is_authenticated:
        return not_authenticated(request)

    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == 'POST':
        form = SettingsForm(request.POST, request.FILES)
        if form.is_valid():
            description = form.data.get('description', None)
            avatar = request.FILES.get('avatar', None)

            if description is not None:
                if description is not profile.description:
                    profile.description = description

            if avatar is not None:
                if avatar.size > 2097152:
                    form.add_error('avatar', "Image is too big! Max 2MB.")
                    return render(request, 'accounts/settings.html', {'form': form})

                if avatar is not profile.avatar:
                    profile.avatar = avatar

            profile.save()
        return redirect('accounts-profile', username=user.username)
    else:
        form = SettingsForm(initial={'description': profile.description, 'avatar': profile.avatar})
        return render(request, 'accounts/settings.html', {'form': form})

