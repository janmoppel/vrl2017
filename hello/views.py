import requests
from django.http import HttpResponse
from django.shortcuts import render

from .models import Greeting


# Create your views here.
def index(request):
    r = requests.get('http://www.google.ee')
    #r = requests.get('http://httpbin.org/status/418')
    #print(r.text)
    return HttpResponse(r.text)
    # return HttpResponse('Hello from Python!')
    # return render(request, 'index.html')


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, 'db.html', {'greetings': greetings})