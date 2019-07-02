from django.test import TestCase
from .forms import UserLoginForm


class TestForms(TestCase):
    def test_login_form(self):
        form = UserLoginForm({'username': 'Test', 'password': 'mypassword'})
        self.assertTrue(form.is_valid())

    def test_login_form_missing_password(self):
        form = UserLoginForm({'username': 'Test', 'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], ['This field is required.'])


class TestViews(TestCase):
    def test_get_index_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_login_page(self):
        page = self.client.get("/accounts/login")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "signin.html")
