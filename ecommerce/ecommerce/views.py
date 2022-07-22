from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def test(request):
    return HttpResponse("Ok!")

def template2(request):
    today = datetime.now().today()
    body = {
        'name': 'Alejandro',
        'lastname': 'Díaz Alvardo',
        'today': today
    }
    return render(request, 'template.html', context=body)

def list_template(request):
    body = {
        'list': ['apple', 'potatoe', 'banana']
    }
    return render(request, 'list_template_example.html', context=body)