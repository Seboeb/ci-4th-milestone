from django.contrib import admin
from .models import BugReport, TicketProgressLabel, TicketPriorityLabel

# Register your models here.
admin.site.register(BugReport)
admin.site.register(TicketProgressLabel)
admin.site.register(TicketPriorityLabel)
