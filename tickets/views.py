from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Ticket, Comment
from .forms import CommentForm, TicketForm
from .utils import create_search_label
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json


def ticket_view(request, id):
    """
    Create a bug report ticket page
    view with details of that ticket
    """
    ticket = get_object_or_404(Ticket, pk=id)
    comments = Comment.objects.filter(ticket=id)

    if request.user.is_authenticated:
        actions = {
            'upvoted': True if request.user.upvotes.all().filter(pk=id) else False,
            'watchlist': True if request.user.watchlist.all().filter(pk=id) else False,
            'owner': True if ticket.user == request.user else False
        }
    else:
        actions = None

    year_range = range(2019, 2039)

    # Calculate domation percentage of ticket

    target_perc = ticket.donated_amount / ticket.target_amount
    if target_perc >= 1:
        target_perc = 1
    donate_info = {
        'circle_offset': round(276 * target_perc),
        'complete': True if target_perc >= 1 else False
    }

    return render(request, 'ticket_view.html', {'ticket': ticket, 'comments': comments, 'actions': actions,
                                                'year_range': year_range, 'publishable': settings.STRIPE_PUBLISHABLE, 'donate_info': donate_info})


@login_required
def post_comment(request):
    """
    Posts a comment for a given ticket view
    """
    if request.method == "POST":

        form = CommentForm(request.POST)

        if form.is_valid():
            # Create comment
            comment = form.save(commit=False)
            comment.user = request.user
            ticket = get_object_or_404(Ticket, pk=request.POST["ticket_id"])
            comment.ticket = ticket
            comment.save()

            # Update ticket
            ticket.nr_comments = ticket.nr_comments + 1
            ticket.save()

        return redirect(ticket_view, request.POST["ticket_id"])


@login_required
def post_bug_report(request):
    """
    Posts a new bug report
    """

    if request.method == "POST":

        # Create new ticket
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.ticket_type_id = 1

            # Set app type
            if request.POST['app_type'] == 'finder_app':
                ticket.finder_app = True
                ticket.recipe_community = False
            elif request.POST['app_type'] == 'recipe_community':
                ticket.finder_app = False
                ticket.recipe_community = True

            # Create ticket id
            number = Ticket.objects.filter(ticket_type=1).count()
            ticket.ticket_id = "B-" + str(number + 1)

            # Create search text
            ticket.search_field = create_search_label(ticket)

            ticket.save()
            request.user.created_tickets.add(ticket)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dev_panel')))


@login_required
def post_feature_request(request):
    """
    Posts a new feature request
    """

    if request.method == "POST":

        # Create new ticket
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.ticket_type_id = 2
            ticket.target_amount = 150.00

            # Set app type
            if request.POST['app_type'] == 'finder_app':
                ticket.finder_app = True
                ticket.recipe_community = False
            elif request.POST['app_type'] == 'recipe_community':
                ticket.finder_app = False
                ticket.recipe_community = True

            # Create ticket id
            number = Ticket.objects.filter(ticket_type=2).count()
            ticket.ticket_id = "F-" + str(number + 1)

            # Create search text
            ticket.search_field = create_search_label(ticket)

            ticket.save()
            request.user.created_tickets.add(ticket)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dev_panel')))


@login_required
def edit_ticket(request):
    """
    Updates the ticket
    """
    if request.method == 'POST':
        # Create new ticket
        form = TicketForm(request.POST)

        if form.is_valid():
            ticket = get_object_or_404(Ticket, pk=request.POST['ticket_id'])
            ticket.title = request.POST['title']
            ticket.description = request.POST['description']
            ticket.search_field = create_search_label(ticket)
            ticket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dev_panel')))


@login_required
@csrf_exempt
def post_upvote(request, id):
    """
    Update the upvote from a user for a specific
    ticket
    """
    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, pk=id)
        ticket_in_list = request.user.upvotes.all().filter(pk=id)

        if ticket_in_list:
            request.user.upvotes.remove(ticket)
            ticket.upvotes = ticket.upvotes - 1
            state = 'off'
        else:
            request.user.upvotes.add(ticket)
            ticket.upvotes = ticket.upvotes + 1
            state = 'on'

        ticket.save()

        return HttpResponse(json.dumps({'status': 'ok', 'state': state, 'upvotes': ticket.upvotes}), content_type='application/json')


@login_required
@csrf_exempt
def post_watchlist(request, id):
    """
    Sets or unsets a ticket from the watchlist
    of a user
    """

    if request.method == 'POST':
        ticket = get_object_or_404(Ticket, pk=id)
        ticket_in_list = request.user.watchlist.all().filter(pk=id)

        if ticket_in_list:
            request.user.watchlist.remove(ticket)
            state = 'off'
        else:
            request.user.watchlist.add(ticket)
            state = 'on'

        return HttpResponse(json.dumps({'status': 'ok', 'state': state}), content_type='application/json')
