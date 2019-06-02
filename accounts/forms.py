from django import forms


class UserLoginForm(forms.Form):
    """Form used to login users """

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
