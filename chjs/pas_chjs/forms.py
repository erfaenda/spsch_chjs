from django import forms
from .models import *
from django.contrib.admin.widgets import AdminDateWidget

class PasForm(forms.Form):
    pas_number = forms.IntegerField(label='Номер паспорта объекта', widget=forms.NumberInput(attrs={"class": "form-control"}))
    mkr_name_pas = forms.ModelChoiceField(label='Район', empty_label='Выберите район', queryset=Mkr_name.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    pas_adress = forms.CharField(label='Адрес', max_length=350, widget=forms.TextInput(attrs={"class": "form-control"}))
    stages = forms.IntegerField(label='Этажей', initial=1, widget=forms.NumberInput(attrs={"class": "form-control"}))
    walls_material = forms.ModelChoiceField(label='Материал стен', empty_label='Выберите материал', queryset=Materials_walls.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    type_heat = forms.ModelChoiceField(label='Тип отопления', empty_label=' Выберите тип', queryset=Type_heat.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    electric = forms.BooleanField(label='Электрофицирован?', initial=True)
    apis = forms.IntegerField(label='Сколько АПИ?', initial=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
    apis_works = forms.IntegerField(label='Исправных АПИ', initial=0 ,widget=forms.NumberInput(attrs={"class": "form-control"}))
    living = forms.IntegerField(label='Проживают', initial=1, widget=forms.NumberInput(attrs={"class": "form-control"}))
    childrens = forms.IntegerField(label='Дети', initial=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
    characteristic = forms.CharField(label='Характеристика проживающих', required=False, widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    owner_name = forms.CharField(label='Собственник', max_length=350, widget=forms.TextInput(attrs={"class": "form-control"}))
    date_owner = forms.DateField(label='Дата', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    woker_mchs = forms.CharField(label='Сотрудник проводивший профобследование', max_length=350, widget=forms.TextInput(attrs={"class": "form-control"}))
    woker_date = forms.DateField(label='Дата', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    #unfineshed = forms.BooleanField(label='Не достроен?', initial=True)
    '''created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    created_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')'''