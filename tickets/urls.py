from django.conf.urls import url
from tickets.views import ticket_view, post_comment, post_bug_report, post_feature_request

urlpatterns = [
    url(r'^(?P<id>\d+)/$', ticket_view, name='ticket_view'),
    url(r'^comment$', post_comment, name='post_comment'),
    url(r'^new-bug', post_bug_report, name='post_bug_report'),
    url(r'^new-feature', post_feature_request, name='post_feature_request'),
]
