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

    app_type = request.GET.get('app', 'finder_app')
    load_more = False

    if app_type == 'finder_app':
        tickets = Ticket.objects.filter(
            finder_app=True, recipe_community=False).order_by('-date_created')
        if tickets.count() > 10:
            load_more = True
            tickets = tickets[:10]

        print(tickets.count())
    elif app_type == 'recipe_community':
        tickets = Ticket.objects.filter(
            finder_app=False, recipe_community=True).order_by('-date_created')[:10]
        if tickets.count() > 10:
            load_more = True
            tickets = tickets[:10]
    else:
        raise Http404

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

    if request.method == 'GET':
        return render(request, 'dev_panel.html', {'tickets': tickets, 'watchlist': watchlist,
                                                  'user_summary': summary, 'created_tickets': created_tickets, 'app_type': app_type, 'load_more': load_more})

    if request.method == 'POST':
        data = serializers.serialize("json", tickets)
        return JsonResponse({'data': data})
