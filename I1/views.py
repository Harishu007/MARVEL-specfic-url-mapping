from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ironman(request):
    return HttpResponse('<h2>ALL TIME FAV</h2>')

def spider(request):
    return HttpResponse('<h1>ALL TIME second Fav</h1>')



