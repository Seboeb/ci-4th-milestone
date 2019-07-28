from django.db import models
from accounts.models import User
from tickets.models import Ticket


class Donation(models.Model):
    amount = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    date = models.DateTimeField(auto_now_add=True)

    # Foreignkeys
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=False)
    ticket = models.ForeignKey(
        Ticket, on_delete=models.CASCADE, blank=False)

    def __str__(self):
        return "{0} {1} donated € {2} for ticket {3}".format(self.user.first_name, self.user.last_name, self.amount, self.ticket.ticket_id)
