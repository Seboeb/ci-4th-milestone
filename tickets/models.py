from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User


class BugReport(models.Model):
    title = models.CharField(max_length=75, default='')
    ticket_id = models.CharField(max_length=10, default='')
    priority = models.CharField(max_length=10, default='low')
    description = models.TextField()
    target_amount = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    finder_app = models.BooleanField(blank=False, default=True)
    recipe_community = models.BooleanField(blank=False, default=False)
    date_created = models.DateTimeField(default=now, editable=False)
    upvotes = models.IntegerField(default=0)
    nr_comments = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title
