from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def blog_index(request):
    return HttpResponse("Blog index page")


def index(request):
    return HttpResponse("Global index page")
