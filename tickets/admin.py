from django.contrib import admin
from .models import Ticket, TicketProgressLabel, TicketPriorityLabel, TicketType, \
    Comment

# Register your models here.
admin.site.register(Ticket)
admin.site.register(TicketProgressLabel)
admin.site.register(TicketPriorityLabel)
admin.site.register(TicketType)
admin.site.register(Comment)
