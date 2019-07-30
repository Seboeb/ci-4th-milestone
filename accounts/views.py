from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserSubscribeForm
from django.http import HttpResponseRedirect


def index(request):
    """
    Returns the index page of the website
    or 'subscribes' person for emailing
    """
    if request.method == "POST":
        subscribe_form = UserSubscribeForm(request.POST)

        if subscribe_form.is_valid():
            messages.success(request, 'Thank you for your email subscription')

    else:
        subscribe_form = UserSubscribeForm()
    return render(request, 'index.html', {'index': True, 'subscribe_form': subscribe_form})


def about(request):
    """
    Returns the about page of the website
    """
    return render(request, 'about.html')


def login(request):
    """
    Return the user login page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(
                email=request.POST['email'], password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                return redirect(reverse('dev_panel'))
            else:
                print('error')
                login_form.add_error(
                    None, 'You have entered an invalid email address or password.')
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})


@login_required
def logout(request):
    """
    The user will be logged out
    """
    auth.logout(request)
    messages.success(request, 'You are logged out!')
    return redirect(reverse('index'))


def registration(request):
    """
    Render and return the user registration page
    """
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(
                email=request.POST['email'], password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, 'You have been registered!')
                return redirect(reverse('index'))
            else:
                messages.error(
                    request, 'Unable to register. Please try again later.')
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'signup.html', {"registration_form": registration_form})


@login_required
def update_user_profile(request):
    """
    Update the user profile information posted 
    by the user_profile diaglog
    """
    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            user = get_object_or_404(User, pk=request.user.pk)
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.profile_picture = request.POST['profile_picture']
            user.save()
            messages.success(request, 'Your profile has been updated!')
        else:
            messages.error(
                request, 'Unable to update your profile. Please try again later.')

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dev_panel')))
