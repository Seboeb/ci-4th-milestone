from django.conf.urls import url, include
from accounts.views import login, logout, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^register/', registration, name='registration'),
    url(r'^profile/', user_profile, name='profile'),
    url(r'password-reset/', include(url_reset))
]
