from django.shortcuts import render
from tickets.models import Ticket


def dev_panel(request):
    """
    Returns the homepage of the dashboard and
    retrieves all the tickets and the personal
    user profile with its watchlist
    """

    tickets = Ticket.objects.all().order_by('-date_created')[:2]
    return render(request, 'dev_panel.html', {'tickets': tickets})
