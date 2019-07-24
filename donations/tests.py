from django.test import TestCase, Client
from django.shortcuts import reverse
from .forms import MakeDonationForm
from .models import Donation
from accounts.models import User
from tickets.models import Ticket


class TestPaymentForms(TestCase):
    def test_payment_form(self):
        form = MakeDonationForm(
            {'amount': 100.00, 'stripe_id': 'afoiwjfoianvoin', 'ticket_id': '1'})
        self.assertTrue(form.is_valid())

    def test_payment_form_amount_required(self):
        form = MakeDonationForm(
            {'amount': '', 'stripe_id': 'afoiwjfoianvoin', 'ticket_id': '1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['amount'], [
                         'This field is required.'])

    def test_payment_form_stipe_id_required(self):
        form = MakeDonationForm(
            {'amount': 100, 'stripe_id': '', 'ticket_id': '1'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['stripe_id'], [
                         'This field is required.'])

    def test_payment_form_ticket_id_required(self):
        form = MakeDonationForm(
            {'amount': 100, 'stripe_id': 'asdfaksf', 'ticket_id': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['ticket_id'], [
                         'This field is required.'])


class TestDonationModel(TestCase):
    def test_create_donation(self):
        user = User(email='test@test.com')
        user.save()
        ticket = Ticket(title='Test', description='My description')
        ticket.save()
        donation = Donation(ticket=ticket, user=user, amount=100)
        donation.save()
        self.assertEqual(donation.amount, 100)
