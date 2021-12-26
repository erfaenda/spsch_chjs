from django import forms
from .models import *

class PasForm(forms.Form):
    pas_number = forms.IntegerField()
    mkr_name_pas = forms.ModelChoiceField(queryset=Mkr_name.objects.all())
    pas_adress = forms.CharField(max_length=350)
    stages = forms.IntegerField()
    walls_material = forms.ModelChoiceField(queryset=Materials_walls.objects.all())
    type_heat = forms.ModelChoiceField(queryset=Type_heat.objects.all())
    electric = forms.BooleanField()
    apis = forms.IntegerField()
    apis_works = forms.IntegerField()
    living = forms.IntegerField()
    childrens = forms.IntegerField()
    characteristic = forms.CharField()
    '''owner_name = forms.CharField(max_length=350)
    date_owner = models.DateField(verbose_name='Дата')
    woker_mchs = forms.CharField(max_length=350)
    woker_date = models.DateField(verbose_name='Дата')
    unfineshed = forms.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    created_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')'''