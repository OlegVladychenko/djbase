from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

import requests
import json
from requests.auth import HTTPBasicAuth
import urllib.parse

from .forms import *
from .models import *
from django.shortcuts import render
from django.template import loader

# menu_directory = ["Контрагенты","Номенклатура","Торговые"]
menu_directory = [{'title': 'Контрагенты', 'ref': 'сlients'}, {'title': 'Номенклатура', 'ref': 'goods'},
                  {'title': 'Торговые', 'ref': 'employees'}]
menu_documents = ["Продажи", "Оплаты", "Возвраты"]
menu_reports = [{'title': 'Продажи', 'ref': 'reports_salary'}, {'title': 'Оплаты', 'ref': 'reports_salary'}, {'title': 'Взаиморасчеты','ref': 'reports_salary'}]


def index(request):
    return render(request, 'trade/index.html',
                  {'menu_directory': menu_directory, 'menu_documents': menu_documents, 'menu_reports': menu_reports})


def сlients(request):
    # url = 'http://localhost/CRM/hs/getClients/'
    # headers = {'Accept': 'application/json'}
    # response = requests.get(url, auth=HTTPBasicAuth('Admin', '123'), headers=headers)
    # response.encoding = 'utf-8-sig'
    # data = json.loads(response.text)

    param_goods = {}
    headers = {'Accept': 'application/json'}
    name_method = "clients"
    url = 'http://localhost/CRM/hs/getClients/' + name_method + "/" + json.dumps(param_goods)
    response = requests.get(url, auth=HTTPBasicAuth('Admin', '123'), headers=headers)
    response.encoding = 'utf-8-sig'
    data = json.loads(response.text)

    return render(request, 'trade/clients.html',
                  {'menu_directory': menu_directory, 'menu_documents': menu_documents, 'menu_reports': menu_reports,
                   'datalist': data})


def goods(request):
    param_goods = {'sender': 'Alice', 'receiver': 'Bob', 'message': 'We did it!'}
    headers = {'Accept': 'application/json'}
    name_method = "goods"
    url = 'http://localhost/CRM/hs/getData/' + name_method + "/" + json.dumps(param_goods)
    response = requests.get(url, auth=HTTPBasicAuth('Admin', '123'), headers=headers)
    response.encoding = 'utf-8-sig'
    data = json.loads(response.text)

    return render(request, 'trade/goods.html',
                  {'menu_directory': menu_directory, 'menu_documents': menu_documents, 'menu_reports': menu_reports,
                   'datalist': data})


def employees(request):
    param_goods = {}
    headers = {'Accept': 'application/json'}
    name_method = "employees"
    url = 'http://localhost/CRM/hs/getData/' + name_method + "/" + json.dumps(param_goods)
    response = requests.get(url, auth=HTTPBasicAuth('Admin', '123'), headers=headers)
    response.encoding = 'utf-8-sig'
    data = json.loads(response.text)

    return render(request, 'trade/employees.html',
                  {'menu_directory': menu_directory, 'menu_documents': menu_documents, 'menu_reports': menu_reports,
                   'datalist': data})


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_сlient(request, client_slug):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.cleaned_data["guid"] = client_slug
            # urllib.parse.quote_plus
            headers = {'Accept': 'application/json', 'Content-type': 'text/plain; charset=utf-8'}
            name_method = "update_client"

            url = 'http://localhost/CRM/hs/getData/' + name_method + "/" + json.dumps(form.cleaned_data,
                                                                                      ensure_ascii=False)
            response = requests.get(url, auth=HTTPBasicAuth('Admin', '123'), headers=headers)
            response.encoding = 'utf-8-sig'
            print(response.status_code)
    else:
        headers = {'Accept': 'application/json'}
        name_method = "get_client"
        url = 'http://localhost/CRM/hs/getData/' + name_method + "/" + client_slug
        response = requests.get(url, auth=HTTPBasicAuth('Admin', '123'), headers=headers)
        response.encoding = 'utf-8-sig'
        data = json.loads(response.text)

        form = ClientForm()
        form.fields["guid"].initial = data.get('GUID')
        form.fields["code"].initial = data.get('Code')
        form.fields["name"].initial = data.get('Name')
        form.fields["full_name"].initial = data.get('FullName')
        form.fields["physical_address"].initial = data.get('PhysicalAddress')
        form.fields["legal_address"].initial = data.get('LegalAddress')
        form.fields["phones"].initial = data.get('Phones')
        form.fields["vat_number"].initial = data.get('Phones')
        form.fields["comment"].initial = data.get('Comment')

    context = {
        'form': form,
        'slug': client_slug,
        'menu_directory': menu_directory,
        'menu_documents': menu_documents,
        'menu_reports': menu_reports,
    }
    return render(request, 'trade/client.html', context)

def reports_salary(request):
    context = {
        'menu_directory': menu_directory,
        'menu_documents': menu_documents,
        'menu_reports': menu_reports,
    }
    return render(request, 'trade/reports_salary.html', context)

def reports_salary_manage(request):
    form = ReportForm()

    datapoints = [
        {"label": "Online Store", "y": 27},
        {"label": "Offline Store", "y": 25},
        {"label": "Discounted Sale", "y": 30},
        {"label": "B2B Channel", "y": 8},
        {"label": "Others", "y": 10}
    ]

    context = {
        'form': form,
        'menu_directory': menu_directory,
        'menu_documents': menu_documents,
        'menu_reports': menu_reports,
        'datapoints': datapoints
    }

    return render(request, 'trade/reports_salary_manage.html', context)

