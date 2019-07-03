from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import BugReport


def bug_report(request, id):
    """
    Create a bug report ticket page
    view with details of that ticket
    """
    bug_report = get_object_or_404(BugReport, pk=id)

    return render(request, 'bug_report.html', {'bug_report': bug_report})
