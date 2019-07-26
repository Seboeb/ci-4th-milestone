from django.test import TestCase, Client
from .forms import UserLoginForm, UserSubscribeForm, UserRegistrationForm, UserProfileForm
from django.shortcuts import reverse
from .models import User


class TestForms(TestCase):
    """
    Testing login, subscribe and 
    registration form
    """

    def test_login_form(self):
        form = UserLoginForm(
            {'email': 'test@test.com', 'password': 'mypassword'})
        self.assertTrue(form.is_valid())

    def test_login_form_false_email(self):
        form = UserLoginForm(
            {'email': 'test', 'password': 'mypassword'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [
                         'Enter a valid email address.'])

    def test_login_form_missing_password(self):
        form = UserLoginForm({'username': 'Test', 'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])

    def test_subscribe_form(self):
        form = UserSubscribeForm({'email': 'test@test.com'})
        self.assertTrue(form.is_valid())

    def test_subscribe_form_false_email(self):
        form = UserSubscribeForm({'email': 'test'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [
                         'Enter a valid email address.'])

    def test_user_register_form(self):
        form = UserRegistrationForm({'email': 'test@test.com', 'first_name': 'Piet',
                                     'last_name': 'Jan', 'password1': 'mypassword', 'password2': 'mypassword'})
        self.assertTrue(form.is_valid())

    def test_user_register_form_false_email(self):
        form = UserRegistrationForm({'email': 'test', 'first_name': 'Piet',
                                     'last_name': 'Jan', 'password1': 'mypassword', 'password2': 'mypassword'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [
                         'Enter a valid email address.'])

    def test_user_register_form_no_email(self):
        form = UserRegistrationForm({'email': '', 'first_name': 'Piet',
                                     'last_name': 'Jan', 'password1': 'mypassword', 'password2': 'mypassword'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [
                         'Please enter an email address'])

    def test_user_register_form_password_confirm_incorrect(self):
        form = UserRegistrationForm({'email': 'test@test.com', 'first_name': 'Piet',
                                     'last_name': 'Jan', 'password1': 'mypassword', 'password2': 'mypassword1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], [
                         'Your passwords are not matching'])

    def test_user_register_form_unique_email(self):
        user = User(email='test@test.com', first_name='Piet', last_name='Jan')
        user.save()
        form = UserRegistrationForm({'email': 'test@test.com', 'first_name': 'Piet',
                                     'last_name': 'Jan', 'password1': 'mypassword', 'password2': 'mypassword1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'], [
                         'Email address must be unique'])

    def test_user_profile_form(self):
        form = UserProfileForm(
            {'first_name': 'Piet', 'last_name': 'Jan', 'profile_picture': 'dummy.png'})
        self.assertTrue(form.is_valid())


class TestViews(TestCase):
    """
    Testing user views regarding
    login, registration, password reset
    and actual login functionality
    """

    def test_get_index_page(self):
        page = self.client.get(reverse('index'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_login_page(self):
        page = self.client.get(reverse('login'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "login.html")

    def test_get_signup_page(self):
        page = self.client.get(reverse('registration'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "signup.html")

    def test_get_password_reset_page(self):
        page = self.client.get(reverse('password_reset'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "registration/password_reset_form.html")

    def test_user_login(self):
        user = User(email='test@test.com')
        user.set_password('mypassword')
        user.save()

        c = Client()
        logged_in = c.login(email='test@test.com', password='mypassword')
        self.assertTrue(logged_in)


class TestUserModel(TestCase):
    """
    Testing the creation of an user
    object
    """

    def test_create_new_user(self):
        user = User(email='test@test.com')
        user.save()
        self.assertEqual(user.email, 'test@test.com')
