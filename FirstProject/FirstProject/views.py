from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Bhanu Reddi")

def menu(request):
    return render(request, "menu.html")