from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *

#menu_directory = ["Контрагенты","Номенклатура","Торговые"]
menu_directory = [{'title':'Контрагенты','ref':'http://127.0.0.1:8000/%D1%81lients/'},{'title':'Номенклатура','ref':'#'},{'title':'Торговые','ref':'#'}]
menu_documents = ["Продажи","Оплаты","Возвраты"]
menu_reports = ["Продажи","Оплаты","Взаиморасчеты"]


def index(request):
    return render(request, 'trade/index.html',{'menu_directory':menu_directory,'menu_documents':menu_documents,'menu_reports':menu_reports})

def сlients(request):
    return render(request, 'trade/clients.html',{'menu_directory':menu_directory,'menu_documents':menu_documents,'menu_reports':menu_reports})

def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')