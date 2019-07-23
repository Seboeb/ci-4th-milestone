from django.shortcuts import render, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import MakeDonationForm
from .models import Donation
from tickets.models import Ticket
from accounts.models import User
from decimal import Decimal
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required
def make_payment(request):
    """
    Make the donation payment possible
    """
    print('incomming!!')
    if request.method == 'POST':
        form = MakeDonationForm(request.POST)

        if form.is_valid():

            if form.cleaned_data['amount'] != 'custom':
                total = Decimal(form.cleaned_data['amount']).quantize(
                    Decimal("1.00"))
            else:
                total = Decimal(form.cleaned_data['custom_amount']).quantize(
                    Decimal("1.00"))

            try:
                customer = stripe.Charge.create(
                    amount=int(total*100),
                    currency="EUR",
                    description="hallo dit is mijn test",
                    card=form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was incorrect or declined.")

            if customer.paid:
                # Update ticket
                ticket = get_object_or_404(
                    Ticket, pk=form.cleaned_data['ticket_id'])
                ticket.donated_amount += total
                ticket.upvotes += 1
                ticket.save()

                # Create donation record
                user = get_object_or_404(User, pk=request.user.pk)
                donation = Donation(amount=total, user=user, ticket=ticket)
                donation.save()

                messages.success(request, "You have successfully paid!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dev_panel')))
            else:
                messages.error(request, "Unable to take payment")

        else:
            print(form.errors)
            messages.error(request, "Payment failed unfortunately")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dev_panel')))
