from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница главная")

def catigories(request):
    return HttpResponse("<h1>Страница торговля</h1>")