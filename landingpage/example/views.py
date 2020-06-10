from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home/home.html', {'page': 'home'})


def about(request):
    return render(request, 'about/about.html', {'page': 'about'})
