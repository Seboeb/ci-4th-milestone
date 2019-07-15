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

        # Create new bug report
        form = TicketForm(request.POST)
        # form.save(commit=False)
        print(form.is_valid())
        print(form.errors)
        print(request.POST)

    return redirect(reverse('dev_panel'))
