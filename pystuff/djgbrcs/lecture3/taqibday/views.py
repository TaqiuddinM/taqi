import datetime
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    return render(request, 'taqibday/index.html', {
        "taqibday": now.month == 1 and now.day == 28
    })

