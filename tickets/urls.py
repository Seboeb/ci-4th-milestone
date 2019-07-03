from django.conf.urls import url
from tickets.views import bug_report

urlpatterns = [
    url(r'bug/(?P<id>\d+)$', bug_report, name='bug_report'),
]
