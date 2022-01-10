from django import forms
from .models import *


# форма на основе полей модели, быстро, просто, молодежно
class MkrForm(forms.ModelForm):
    class Meta:
        model = Mkr_name
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"})
        }


class MaterialsWallsForm(forms.ModelForm):
    class Meta:
        model = Materials_walls
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"})
        }


class TypeHeatForm(forms.ModelForm):
    class Meta:
        model = Type_heat
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={"class": "form-control"})
        }


class EditPasForm(forms.ModelForm):
    class Meta:
        model = Pas_chjs
        fields = ['pas_number', 'mkr_name_pas', 'pas_adress', 'stages', 'walls_material', 'type_heat',
                  'electric', 'apis', 'apis_works', 'living', 'childrens', 'characteristic', 'owner_name',
                  'date_owner', 'woker_mchs', 'woker_date']
        widgets = {
            'pas_number': forms.NumberInput(attrs={"class": "form-control"}),
            'mkr_name_pas': forms.Select(attrs={"class": "form-control"}),
            'pas_adress': forms.TextInput(attrs={"class": "form-control"}),
            'stages': forms.NumberInput(attrs={"class": "form-control"}),
            'walls_material': forms.Select(attrs={"class": "form-control"}),
            'type_heat': forms.Select(attrs={"class": "form-control"}),
            'electric': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px;margin:1em;'}),
            # сразу тут задал стиль для чекбокса
            'apis': forms.NumberInput(attrs={"class": "form-control"}),
            'apis_works': forms.NumberInput(attrs={"class": "form-control"}),
            'living': forms.NumberInput(attrs={"class": "form-control"}),
            'childrens': forms.NumberInput(attrs={"class": "form-control"}),
            'characteristic': forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            'owner_name': forms.TextInput(attrs={"class": "form-control"}),
            'date_owner': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 'placeholder': 'Выберете дату', 'type': 'date'}),
            'woker_mchs': forms.TextInput(attrs={"class": "form-control"}),
            'woker_date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={'class': 'form-control', 'placeholder': 'Выберете дату', 'type': 'date'}),
            # выше виджет даты такого вида потому что надо виджет не коректно понимает формат при редактировании
        }


class PasForm(forms.Form):
    pas_number = forms.IntegerField(label='Номер паспорта объекта',
                                    widget=forms.NumberInput(attrs={"class": "form-control"}))
    mkr_name_pas = forms.ModelChoiceField(label='Район', empty_label='Выберите район', queryset=Mkr_name.objects.all(),
                                          widget=forms.Select(attrs={"class": "form-control"}))
    pas_adress = forms.CharField(label='Адрес', max_length=350, widget=forms.TextInput(attrs={"class": "form-control"}))
    stages = forms.IntegerField(label='Этажей', initial=1, widget=forms.NumberInput(attrs={"class": "form-control"}))
    walls_material = forms.ModelChoiceField(label='Материал стен', empty_label='Выберите материал',
                                            queryset=Materials_walls.objects.all(),
                                            widget=forms.Select(attrs={"class": "form-control"}))
    type_heat = forms.ModelChoiceField(label='Тип отопления', empty_label=' Выберите тип',
                                       queryset=Type_heat.objects.all(),
                                       widget=forms.Select(attrs={"class": "form-control"}))
    electric = forms.BooleanField(label='Электрофицирован?', initial=True)
    apis = forms.IntegerField(label='Сколько АПИ?', initial=0,
                              widget=forms.NumberInput(attrs={"class": "form-control"}))
    apis_works = forms.IntegerField(label='Исправных АПИ', initial=0,
                                    widget=forms.NumberInput(attrs={"class": "form-control"}))
    living = forms.IntegerField(label='Проживают', initial=1, widget=forms.NumberInput(attrs={"class": "form-control"}))
    childrens = forms.IntegerField(label='Дети', initial=0, widget=forms.NumberInput(attrs={"class": "form-control"}))
    characteristic = forms.CharField(label='Характеристика проживающих', required=False,
                                     widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    owner_name = forms.CharField(label='Собственник', max_length=350,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    date_owner = forms.DateField(label='Дата', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    woker_mchs = forms.CharField(label='Сотрудник проводивший профобследование', max_length=350,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    woker_date = forms.DateField(label='Дата', widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    # unfineshed = forms.BooleanField(label='Не достроен?', initial=True)
    '''created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    created_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')'''
