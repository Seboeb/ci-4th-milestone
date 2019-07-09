from django.shortcuts import render


def dev_panel(request):
    """Returns the homepage of the dashboard"""

    return render(request, 'dev_panel.html')
