from django.conf.urls import url
from tickets.views import bug_report

urlpatterns = [
    url(r'(?P<id>\d+)$', bug_report, name='bug_report'),
]
