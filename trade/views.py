from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

menu = ["Контрагенты","Номенклатура","Торговые"]

def index(request):
    return render(request, 'trade/index.html',{'menu':menu})

def сlients(request):
    return render(request, 'trade/clients.html')

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')