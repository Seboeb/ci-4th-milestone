from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm


def index(request):
    """Returns the index page of the website"""
    return render(request, 'index.html')


def login(request):
    """Return the user login page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        print(request.POST)
        login_form = UserLoginForm(request.POST)
        print(login_form)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'], password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You are logged in!')
                return redirect(reverse('index'))
            else:
                login_form.add_error(
                    None, 'You have entered an invalid username or password.')
    else:
        login_form = UserLoginForm()
    return render(request, 'signin.html', {'login_form': login_form})


@login_required
def logout(request):
    """The user will be logged out"""
    auth.logout(request)
    messages.success(request, 'You are logged out!')
    return redirect(reverse('index'))


def registration(request):
    """Render and return the user registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()

            user = auth.authenticate(
                username=request.POST['username'], password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have been registered!')
                return redirect(reverse('index'))
            else:
                messages.error(
                    request, 'Unable to register. Please try again later.')
        else:
            print(registration_form.errors)
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'signup.html', {"registration_errors": registration_form.errors})


def user_profile(request):
    """Return the users profile page"""
    user = User.objects.get(email=request.user.email)
    return render(request, 'profile_page.html', {"profile": user})
