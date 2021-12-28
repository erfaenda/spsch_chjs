from django import forms
from .models import *

class PasForm(forms.Form):
    pas_number = forms.IntegerField(label='Номер паспорта объекта', widget=forms.NumberInput(attrs={"class": "form-control"}))
    mkr_name_pas = forms.ModelChoiceField(label='Район', empty_label='Выберите район', queryset=Mkr_name.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    pas_adress = forms.CharField(label='Адрес', max_length=350, widget=forms.TextInput(attrs={"class": "form-control"}))
    stages = forms.IntegerField(label='Этажей', widget=forms.NumberInput(attrs={"class": "form-control"}))
    walls_material = forms.ModelChoiceField(label='Материал стен', empty_label='Выберите материал', queryset=Materials_walls.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    type_heat = forms.ModelChoiceField(label='Тип отопления', empty_label=' Выберите тип', queryset=Type_heat.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    electric = forms.BooleanField(label='Электрофицирован?', initial=True)
    apis = forms.IntegerField(label='Сколько АПИ?', widget=forms.NumberInput(attrs={"class": "form-control"}))
    apis_works = forms.IntegerField(label='Исправных АПИ', widget=forms.NumberInput(attrs={"class": "form-control"}))
    living = forms.IntegerField(label='Проживают', widget=forms.NumberInput(attrs={"class": "form-control"}))
    childrens = forms.IntegerField(label='Дети', widget=forms.NumberInput(attrs={"class": "form-control"}))
    characteristic = forms.CharField(label='Характеристика проживающих', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    owner_name = forms.CharField(label='Собственник', max_length=350, widget=forms.TextInput(attrs={"class": "form-control"}))
    date_owner = forms.DateField(label='Дата', widget=forms.DateInput(attrs={"class": "form-control"}))
    woker_mchs = forms.CharField(label='Сотрудник проводивший профобследование', max_length=350, widget=forms.TextInput(attrs={"class": "form-control"}))
    woker_date = forms.DateField(label='Дата', widget=forms.DateInput(attrs={"class": "form-control"}))
    unfineshed = forms.BooleanField(label='Не достроен?', initial=True)
    '''created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    created_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')'''