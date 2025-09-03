from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return  HttpResponse("Home Page")
    return render(request, "website/index.html")


def about(request):
    return  HttpResponse("About Page")


def contact(request):
    return  HttpResponse("Contact Page")