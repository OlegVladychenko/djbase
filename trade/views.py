from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Страница торговля")

def catigories(request):
    return HttpResponse("Страница торговля")