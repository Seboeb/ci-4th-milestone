from django.conf.urls import url
from donations.views import make_payment

urlpatterns = [
    url(r'^$', make_payment, name='make_payment'),
]
