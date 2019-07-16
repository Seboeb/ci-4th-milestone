from django.shortcuts import render
from tickets.models import Ticket


def dev_panel(request):
    """
    Returns the homepage of the dashboard and
    retrieves all the tickets and the personal
    user profile with its watchlist
    """

    tickets = Ticket.objects.all().order_by('-date_created')[:10]

    if request.user.is_authenticated:
        watchlist = request.user.watchlist.all()
        created_tickets = request.user.created_tickets.all()
        summary = {
            'nr_bugs': Ticket.objects.filter(user=request.user, ticket_type=1).count(),
            'nr_features': Ticket.objects.filter(user=request.user, ticket_type=2).count()
        }
    else:
        watchlist = None
        summary = None
        created_tickets = None

    return render(request, 'dev_panel.html', {'tickets': tickets, 'watchlist': watchlist,
                                              'user_summary': summary, 'created_tickets': created_tickets})
