from django.test import TestCase
from django.shortcuts import reverse


class TestViewsDevPanel(TestCase):
    def test_dev_panel_page(self):
        page = self.client.get(reverse('dev_panel'))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "dev_panel.html")
