from django.shortcuts import redirect


def index(request):
    url = '/blog/'
    return redirect(url)
