from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Ticket, Comment
from .forms import CommentForm, TicketForm
from django.contrib.auth.decorators import login_required


def ticket_view(request, id):
    """
    Create a bug report ticket page
    view with details of that ticket
    """
    ticket = get_object_or_404(Ticket, pk=id)
    comments = Comment.objects.filter(ticket=id)

    return render(request, 'ticket_view.html', {'ticket': ticket, 'comments': comments})


@login_required
def post_comment(request):
    """
    Posts a comment for a given ticket view
    """
    if request.method == "POST":

        form = CommentForm(request.POST)
        print(form.is_valid())
        print(form.errors)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            ticket = get_object_or_404(Ticket, pk=request.POST["ticket_id"])
            comment.ticket = ticket
            comment.save()

        return redirect(ticket_view, request.POST["ticket_id"])

        # comment = Comment.objects.create(
        #     comment="Dit is een test lol2", ticket=ticket)
        # comment.save()


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
            ticket.save()

    return redirect(reverse('dev_panel'))


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
            ticket.save()

    return redirect(reverse('dev_panel'))
