from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages

from accounts.forms import UserLoginForm


def index(request):
    """Returns the index page of the website"""
    return render(request, 'index.html')


def login(request):
    """Return the user login page"""
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                username=request.POST['username'], password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You are logged in!')
            else:
                login_form.add_error(
                    None, 'You have entered an invalid username or password.')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


def logout(request):
    """The user will be logged out"""
    auth.logout(request)
    messages.success(request, 'You are logged out!')
    return redirect(reverse('index'))
