from django.test import TestCase
from django.shortcuts import reverse, get_object_or_404
from .forms import CommentForm, TicketForm
from .models import Ticket, TicketProgressLabel, TicketPriorityLabel, TicketType, Comment
from accounts.models import User


class TestCommentForms(TestCase):
    """
    Tests for the comment forms
    """

    def test_comment_form(self):
        form = CommentForm({'comment': 'This is my comment'})
        self.assertTrue(form.is_valid())

    def test_comment_form_no_input(self):
        form = CommentForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['comment'], ['This field is required.'])


class TestTicketForms(TestCase):
    """
    Tests for the ticket forms
    """

    def test_ticket_form(self):
        form = TicketForm({'title': 'This is my title',
                           'description': 'This is my description'})
        self.assertTrue(form.is_valid())

    def test_comment_form_no_input(self):
        form = TicketForm({'title': '', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['title'], ['This field is required.'])
        self.assertEqual(form.errors['description'], [
                         'This field is required.'])


class TestTicketModel(TestCase):
    """
    Testing the ticket model, ticket progress label,
    ticket priority label, ticket type and comment
    models
    """

    def test_create_new_ticket(self):
        ticket = Ticket(title='Test title', description='Test description')
        ticket.save()
        self.assertFalse(ticket.finder_app)
        self.assertFalse(ticket.recipe_community)
        self.assertEqual(ticket.estimate_devtime, 'unknown at this moment.')
        self.assertEqual(ticket.target_amount, 0)
        self.assertEqual(ticket.donated_amount, 0)
        self.assertEqual(ticket.upvotes, 0)
        self.assertEqual(ticket.nr_comments, 0)

    def test_create_new_progress_label(self):
        label = TicketProgressLabel(label_name='test')
        label.save()
        self.assertEqual(label.label_name, 'test')

    def test_create_new_priority_label(self):
        label = TicketPriorityLabel(label_name='test')
        label.save()
        self.assertEqual(label.label_name, 'test')

    def test_create_new_ticket_type(self):
        label = TicketType(name='test')
        label.save()
        self.assertEqual(label.name, 'test')

    def test_create_new_comment(self):
        user = User(email='test@test.com').save()
        ticket = Ticket(title='Test title',
                        description='Test description').save()

        comment = Comment(comment='This is a test comment',
                          user=user, ticket=ticket)
        comment.save()
        self.assertEqual(comment.user, user)
        self.assertEqual(comment.ticket, ticket)
        self.assertEqual(comment.comment, 'This is a test comment')


class TestTicketViews(TestCase):
    """
    Testing the ticket url views
    Including ticket view,
    Ticket view when no ticket exists,
    Comment for ticket,
    New bug report,
    New feature request,
    Ticket upvote
    Ticket watchlist
    """

    def test_ticket_view_page(self):
        ticket = create_ticket()

        page = self.client.get(
            reverse('ticket_view', kwargs={'id': ticket.pk}))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'ticket_view.html')

    def test_ticket_view_page_no_ticket(self):
        page = self.client.get(reverse('ticket_view', kwargs={'id': '1'}))
        self.assertEqual(page.status_code, 404)

    def test_comment_for_ticket(self):
        ticket = create_ticket()
        self.assertEqual(ticket.nr_comments, 0)

        user = create_user()
        logged_in = self.client.login(
            email='test@test.com', password='mypassword')
        self.assertTrue(logged_in)

        page = self.client.post(reverse('post_comment'), {
                                'comment': 'my comment', 'ticket_id': ticket.pk}, follow=True)
        self.assertEqual(page.status_code, 200)

        updated_ticket = get_object_or_404(Ticket, pk=ticket.pk)
        self.assertEqual(updated_ticket.nr_comments, 1)

    def test_new_bug_report(self):
        ticket_type1 = TicketType(name='bug_report').save()
        ticket_type2 = TicketType(name='feature_request').save()
        user = create_user()
        logged_in = self.client.login(
            email='test@test.com', password='mypassword')
        self.assertTrue(logged_in)

        # Post data
        page = self.client.post(reverse('post_bug_report'), {
                                'title': 'Test Title', 'description': 'My test description', 'app_type': 'finder_app'}, follow=True)
        self.assertEqual(page.status_code, 200)

        ticket = get_object_or_404(Ticket, pk='1')
        self.assertEqual(ticket.title, 'Test Title')
        self.assertEqual(ticket.description, 'My test description')
        self.assertEqual(ticket.ticket_type.name, 'bug_report')

    def test_new_feature_request(self):
        ticket_type1 = TicketType(name='bug_report').save()
        ticket_type2 = TicketType(name='feature_request').save()
        user = create_user()
        logged_in = self.client.login(
            email='test@test.com', password='mypassword')
        self.assertTrue(logged_in)

        # Post data
        page = self.client.post(reverse('post_feature_request'), {
                                'title': 'Test Title', 'description': 'My test description', 'app_type': 'finder_app'}, follow=True)
        self.assertEqual(page.status_code, 200)

        ticket = get_object_or_404(Ticket, pk='1')
        self.assertEqual(ticket.title, 'Test Title')
        self.assertEqual(ticket.description, 'My test description')
        self.assertEqual(ticket.ticket_type.name, 'feature_request')

    def test_upvote(self):
        ticket = create_ticket()
        user = create_user()
        logged_in = self.client.login(
            email='test@test.com', password='mypassword')
        self.assertTrue(logged_in)

        page = self.client.post(reverse('post_upvote', kwargs={
                                'id': ticket.pk}), follow=True)
        self.assertEqual(page.status_code, 200)

        updated_ticket = get_object_or_404(Ticket, pk=ticket.pk)
        self.assertEqual(updated_ticket.upvotes, 1)

    def test_watchlist(self):
        ticket = create_ticket()
        user = create_user()
        logged_in = self.client.login(
            email='test@test.com', password='mypassword')
        self.assertTrue(logged_in)

        page = self.client.post(reverse('post_watchlist', kwargs={
                                'id': ticket.pk}), follow=True)
        self.assertEqual(page.status_code, 200)
        self.assertEqual(user.watchlist.all()[0], ticket)


"""
Helper functions for testing
"""


def create_ticket():
    ticket_type1 = TicketType(name='bug_report').save()
    ticket_type2 = TicketType(name='feature_request').save()
    ticket = Ticket(title='Test title',
                    description='Test description')
    ticket.save()
    return ticket


def create_user():
    user = User(email='test@test.com')
    user.set_password('mypassword')
    user.save()
    return user
