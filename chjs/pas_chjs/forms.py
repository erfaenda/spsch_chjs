from django import forms
from .models import *

class PasForm(forms.Form):
    pas_number = forms.IntegerField(label='Номер паспорта объекта', widget=forms.NumberInput(attrs={"class": "form-control"}))
    mkr_name_pas = forms.ModelChoiceField(label='Район', empty_label='Выберите район', queryset=Mkr_name.objects.all(), widget=forms.Select(attrs={"class": "form-control"}))
    pas_adress = forms.CharField(label='Адрес', max_length=350, widget=<div class="mb-3">
        <label for="{{ form.mkr_name_pas.id_for_lable }}" class="form-label">Район:</label>
        {{ form.mkr_name_pas }}
        <div class="invalid-feedback">
            {{ form.mkr_name_pas.errors }}
        </div>
    </div>)
    stages = forms.IntegerField(label='Этажей')
    walls_material = forms.ModelChoiceField(label='Материал стен', empty_label='Выберите материал', queryset=Materials_walls.objects.all())
    type_heat = forms.ModelChoiceField(label='Тип отопления', empty_label=' Выберите тип', queryset=Type_heat.objects.all())
    electric = forms.BooleanField(label='Электрофицирован?', initial=True)
    apis = forms.IntegerField(label='Сколько АПИ?')
    apis_works = forms.IntegerField(label='Исправных АПИ')
    living = forms.IntegerField(label='Проживают')
    childrens = forms.IntegerField(label='Дети')
    characteristic = forms.CharField(label='Краткая характеристика проживающих', required=False, widget=forms.Textarea)
    '''owner_name = forms.CharField(max_length=350)
    date_owner = models.DateField(verbose_name='Дата')
    woker_mchs = forms.CharField(max_length=350)
    woker_date = models.DateField(verbose_name='Дата')
    unfineshed = forms.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    created_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')'''