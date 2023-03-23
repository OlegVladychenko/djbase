from django import forms
from .models import *

class ClientForm(forms.Form):
    guid = forms.CharField(max_length=50,required=False,label="Идентификатор")
    code = forms.CharField(max_length=20,label="Номер")
    name = forms.CharField(max_length=250,label="Наименование")
    vat_number = forms.CharField(max_length=20,required=False,label="ИНН")
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols':10,'rows':10}),required=False,label="Комментарий")