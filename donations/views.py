from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import MakeDonationForm
from django.conf import settings
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
            total = 10
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
                print('customer paid!')
                messages.success(request, "You have successfully paid!")
                return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dev_panel')))
            else:
                messages.error(request, "Unable to take payment")

        else:
            print(form.errors)
            messages.error(request, "Payment failed unfortunately")

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('dev_panel')))
