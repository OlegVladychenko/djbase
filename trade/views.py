from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

menu = ["Контрагенты","Номенклатура","Торговые"]

def index(request):
    return render(request, 'trade/index.html',{'menu':menu})

def сlients(request):
    return render(request, 'trade/clients.html',{'menu':menu})

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')