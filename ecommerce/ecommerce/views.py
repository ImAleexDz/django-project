from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("Ok!")

def template(request):
    return render(request, 'template.html', context={})