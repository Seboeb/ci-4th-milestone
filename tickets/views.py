from django.shortcuts import render

# Create your views here.


def bug_report(request, id):
    """Return a bug report ticket page"""
    print(id)
    return render(request, 'bug_report.html')
