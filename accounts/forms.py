from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form used to login users """

    email = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email):
            raise forms.ValidationError('Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError('Please confirm your password')

        if password1 != password2:
            raise forms.ValidationError('Your passwords are not matching')

        return password2

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise forms.ValidationError('Please enter a first name')

        return first_name

    def clean_last_name(self):
        first_name = self.cleaned_data.get('last_name')

        if not first_name:
            raise forms.ValidationError('Please enter a last name')

        return first_name


class UserProfileForm(forms.ModelForm):
    """
    This form is used to update the user profile
    information
    """

    class Meta:
        model = User
        fields = ['profile_picture', 'first_name', 'last_name']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise forms.ValidationError('Please enter a first name')

        return first_name

    def clean_last_name(self):
        first_name = self.cleaned_data.get('last_name')

        if not first_name:
            raise forms.ValidationError('Please enter a last name')

        return first_name
