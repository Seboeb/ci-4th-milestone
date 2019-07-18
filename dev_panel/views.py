from django.shortcuts import render
from tickets.models import Ticket
from django.http import Http404, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json


@csrf_exempt
def dev_panel(request):
    """
    Returns the homepage of the dashboard and
    retrieves all the tickets and the personal
    user profile with its watchlist
    """

    # Get request parameters
    try:
        app_type = request.GET.get('app', 'finder_app')
        query = request.GET.get('query', '')
        start_range = int(request.GET.get('start', '1')) - 1
        limit_range = int(request.GET.get('limit', '10'))
    except:
        raise Http404

    # Get tickets from correct app
    if app_type == 'finder_app':
        tickets = Ticket.objects.filter(
            finder_app=True, recipe_community=False).order_by('-date_created')
    elif app_type == 'recipe_community':
        tickets = Ticket.objects.filter(
            finder_app=False, recipe_community=True).order_by('-date_created')
    else:
        raise Http404

    if query != '':
        tickets = tickets.filter(search_field__contains=query.lower())

    # Select range of the tickets
    if tickets.count() > start_range + limit_range:
        load_more = True
        tickets = tickets[start_range:start_range+limit_range]
    else:
        load_more = False
        tickets = tickets[start_range:]

    # For authenticated users only (dashboard and watchlist)
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

    # Send response
    if request.method == 'GET':
        return render(request, 'dev_panel.html', {'tickets': tickets, 'watchlist': watchlist,
                                                  'user_summary': summary, 'created_tickets': created_tickets, 'app_type': app_type, 'load_more': load_more})
    if request.method == 'POST':
        ticket_data = [get_ticket_data(ticket) for ticket in tickets]
        return HttpResponse(json.dumps({'load_more': load_more, 'data': ticket_data}), content_type='application/json')


def get_ticket_data(ticket):
    return {
        'id': ticket.pk,
        'user_name': ticket.user.first_name + ' ' + ticket.user.last_name,
        'date_created': ticket.date_created.strftime('%d %b, %Y'),
        'ticket_type': ticket.ticket_type.name,
        'title': ticket.title,
        'ticket_id': ticket.ticket_id,
        'nr_comments': ticket.nr_comments,
        'upvotes': ticket.upvotes
    }
