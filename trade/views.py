from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница главная")

def сlients(request):
    return HttpResponse("<h1>Контрагенты</h1>")

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')