from django.db import models
from django.utils.timezone import now
from accounts.models import User


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=10, default='')
    title = models.CharField(max_length=75, default='')
    description = models.TextField()
    finder_app = models.BooleanField(blank=False, default=False)
    recipe_community = models.BooleanField(blank=False, default=False)
    estimate_devtime = models.CharField(
        max_length=75, default='unknown at this moment.')
    target_amount = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    donated_amount = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)

    date_created = models.DateTimeField(auto_now_add=True)
    upvotes = models.IntegerField(default=0)
    nr_comments = models.IntegerField(default=0)

    # Foreignkeys
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey(
        'TicketProgressLabel', on_delete=models.CASCADE, default=1)
    priority = models.ForeignKey(
        'TicketPriorityLabel', on_delete=models.CASCADE, default=1)
    ticket_type = models.ForeignKey(
        'TicketType', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class TicketProgressLabel(models.Model):
    label_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.label_name


class TicketPriorityLabel(models.Model):
    label_name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.label_name


class TicketType(models.Model):
    name = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.name


class Comment(models.Model):
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    # Foreignkeys
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    ticket = models.ForeignKey(
        'Ticket', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comment
