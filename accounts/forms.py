from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserLoginForm(forms.Form):
    """Form used to login users """

    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput)


class UserSubscribeForm(forms.Form):
    """
    Form used to subscribe a user for
    email notification
    """
    email = forms.EmailField(required=False)

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError('Please enter an email address')

        return email


class UserRegistrationForm(UserCreationForm):
    """Form used to register a new user"""

    email = forms.EmailField(required=False)
    password1 = forms.CharField(widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if not email:
            raise forms.ValidationError('Please enter an email address')

        if User.objects.filter(email=email):
            raise forms.ValidationError('Email address must be unique')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 and not password2:
            raise forms.ValidationError('Please enter a password')

        if not password1 or not password2:
            raise forms.ValidationError('Please confirm your password')

        if password1 != password2:
            raise forms.ValidationError('Your passwords are not matching')

        return password2

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if not first_name:
            raise forms.ValidationError('Please enter a first name')

        if len(first_name) > 30:
            raise forms.ValidationError(
                'A maximan of 30 characters is allowed for your first name')

        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')

        if not last_name:
            raise forms.ValidationError('Please enter a last name')

        if len(last_name) > 30:
            raise forms.ValidationError(
                'A maximan of 30 characters is allowed for your last name')

        return last_name


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
