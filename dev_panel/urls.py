from django.conf.urls import url
from .views import dev_panel

urlpatterns = [
    url(r'^$', dev_panel, name='dev_panel'),
]
