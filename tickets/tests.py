from django.test import TestCase
from .models import BugReport

# Create your tests here.


class BugReportTests(TestCase):
    """
    Testing the Bug Report models
    """

    def test_bug_report_title(self):
        bug_report = BugReport(title='Bug Report')
        bug_report.save()
        self.assertEqual(str(bug_report), 'Bug Report')

    def test_default_values_bug_report(self):
        bug_report = BugReport(title='My Bug Report')
        bug_report.save()
        self.assertTrue(bug_report.finder_app)
        self.assertFalse(bug_report.recipe_community)
        self.assertEqual(bug_report.target_amount, 0.00)
        self.assertEqual(bug_report.description, '')
        self.assertEqual(bug_report.priority, 'low')
        self.assertEqual(bug_report.upvotes, 0)
        self.assertEqual(bug_report.nr_comments, 0)
