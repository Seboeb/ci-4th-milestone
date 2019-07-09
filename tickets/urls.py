from django.conf.urls import url
from tickets.views import ticket_view, post_comment

urlpatterns = [
    url(r'^(?P<id>\d+)/$', ticket_view, name='ticket_view'),
    url(r'^comment$', post_comment, name='post_comment'),
]
