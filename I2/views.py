from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def wanda(request):
    return HttpResponse('<marquee><h1>magical girl</h1></marquee>')

def vision(request):
    return HttpResponse('<marquee><h1>vanda husband</h1></marquee>')
