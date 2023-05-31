from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

import datetime
import requests
import json
from requests.auth import HTTPBasicAuth
import urllib.parse
from html import unescape

from .forms import *
from .models import *
from .utils import *
from django.shortcuts import render
from django.template import loader
from django.db.models import Q

from .report_utils import *

# menu_directory = ["Контрагенты","Номенклатура","Торговые"]
menu_directory = [{'title': 'Контрагенты', 'ref': 'сlients'}, {'title': 'Номенклатура', 'ref': 'goods'},
                  {'title': 'Торговые', 'ref': 'employees'}]
menu_documents = ["Продажи", "Оплаты", "Возвраты"]
menu_reports = [{'title': 'Продажи', 'ref': 'reports_salary'},
                {'title': 'Оплаты', 'ref': 'reports_salary'},
                {'title': 'Взаиморасчеты', 'ref': 'reports_salary'},
                {'title': 'Валюты', 'ref': 'reports_currencies'}
                ]


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
    }
    c_def = DataMixin.get_menu_context()
    context = dict(list(context.items()) + list(c_def.items()))
    return render(request, 'trade/client.html', context)


def reports_salary(request):
    context = DataMixin.get_menu_context()
    return render(request, 'trade/reports_salary.html', context)

def reports_currencies(request):
    context = DataMixin.get_menu_context()
    return render(request, 'trade/reports_currencies.html', context)


def reports_salary_manage(request):
    managers = {}
    percents = {}
    colors = {}
    total = 0
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            headers = {'Accept': 'application/json', 'Content-type': 'text/plain; charset=utf-8'}
            name_method = "reports_salary_manage"
            print(form.cleaned_data.get('date_start').isoformat())
            params = {'date_start': form.cleaned_data.get('date_start').strftime("%Y%m%d"),
                      'date_end': form.cleaned_data.get('date_end').strftime("%Y%m%d")}

            url = 'http://localhost/CRM/hs/getData/' + name_method + "/" + json.dumps(params, ensure_ascii=False)
            response = requests.get(url, auth=HTTPBasicAuth('Admin', '123'), headers=headers)
            response.encoding = 'utf-8-sig'
            data = json.loads(response.text)
            print(response.status_code)
            print(data)

            managers = data[0].get('Manager')
            percents = data[0].get('Percent')
            colors = get_colors(len(managers))
            total = data[0].get('Total')
            print(managers)
            print(percents)
    else:
        form = ReportForm()

    context = {
        'form': form,
        'managers': managers,
        'percents': percents,
        'colors': colors,
        'total': total,
    }
    c_def = DataMixin.get_menu_context()
    context = dict(list(context.items()) + list(c_def.items()))
    return render(request, 'trade/reports_salary_manage.html', context)

def reports_currencies_uah(request):
    if request.method == 'POST':
        form = ReportForm(request.POST)
        d1 = date(2018, 8, 13)  # начальная дата
        d2 = date(2018, 9, 13)
        print(get_array_date_between(d1, d2))
    else:
        form = ReportForm()
    context = {
        'form': form
    }
    c_def = DataMixin.get_menu_context()
    context = dict(list(context.items()) + list(c_def.items()))
    return render(request, 'trade/reports_currencies_uah.html', context)


class NotesList(DataMixin, ListView):
    paginate_by = 15
    template_name = 'trade/notes.html'

    def get_queryset(self, **kwargs):
        params = self.request.GET.get('query', None)
        if params is None:
            return Notes.objects.all()
        else:
            return Notes.objects.filter(
                Q(content__icontains=params)
            )

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        params = self.request.GET.get('query', None)
        if params is not None:
            context['search'] = params
        else:
            context['search'] = ''

        c_def = self.get_user_context()
        return dict(list(context.items())+list(c_def.items()))


def show_note(request, note_id):

    note = get_object_or_404(Notes, pk=note_id)
    print(request.method)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            try:
                form.save()
            except:
                form.add_error(None, 'Ошибка добавления заметки')
    else:
        form = NoteForm(instance=note)

    context = {
        'note_id': note_id,
        'form': form,
    }
    c_def = DataMixin.get_menu_context()
    context = dict(list(context.items()) + list(c_def.items()))

    return render(request, 'trade/note.html', context)

class AddNote(DataMixin,CreateView):
    form_class = NoteForm
    template_name = 'trade/add_note.html'
    success_url = reverse_lazy('notes')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context()
        return dict(list(context.items()) + list(c_def.items()))


#def add_note(request):
    #    if request.method == 'POST':
    #    form = NoteForm(request.POST)
    #    if form.is_valid():
    #        try:
    #            form.save()
    #            return redirect('notes')
    #        except:
    #            form.add_error(None, 'Ошибка добавления заметки')
    # else:
    #    form = NoteForm()
    # context = {
    #    'form': form,
    #    'menu_directory': menu_directory,
    #    'menu_documents': menu_documents,
    #    'menu_reports': menu_reports,
    # }
# return render(request, 'trade/add_note.html', context)

def delete_note(request, note_id):
    try:
        instance = Notes.objects.get(id=note_id)
        instance.delete()
        return redirect('notes')
    except:
        print('Ошибка удаления заметки')
    return render(request)