from django.shortcuts import render
from django.http import HttpResponse

def HomePageView(request):
    return render(request, "home.html")

def AboutPageView(request):
    return render(request, "about.html")