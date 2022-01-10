from django.shortcuts import render, redirect
from django.db.models import *
from django.http import HttpResponse
from .forms import *
from django.views.generic import ListView
from django.core.paginator import Paginator

from .models import *

def index(request):
    pas_chjs = Pas_chjs.objects.all()
    mkr_name = Mkr_name.objects.all()
    materials_walls = Materials_walls.objects.all()
    objects = Pas_chjs.objects.all()
    paginator = Paginator(objects, 100)
    page_num = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_num)

    context = {
        'pas_chjs': pas_chjs,
        'title': 'Список паспортов ЧЖС',
        'mkr_name': mkr_name,
        'materials_wals': materials_walls,
        'page_obj': page_objects,
    }
    return render(request, 'pas_chjs/index.html', context)

def get_mkr_name(request, mkr_name_pas_id):
    pas_chjs = Pas_chjs.objects.filter(mkr_name_pas_id=mkr_name_pas_id)
    mkr_names = Mkr_name.objects.all()
    mkr_name = Mkr_name.objects.get(pk=mkr_name_pas_id)
    return render(request, 'pas_chjs/mkr.html', {'pas_chjs': pas_chjs, 'mkr_names': mkr_names,
                                                 'mkr_name': mkr_name, })

def get_pas(request, id):
    pas_chjs = Pas_chjs.objects.filter(id=id)
    id_pas = Pas_chjs.objects.get(pk=id)
    context = {
        'pas_chjs': pas_chjs,
        'id_pas': id_pas,
        #'pas_all': pas_all,
    }
    return render(request, 'pas_chjs/blank_chjs.html', context)

# def pas_edit(request, id):
#     pas_chjs = Pas_chjs.objects.filter(id=id)
#     id_pas = Pas_chjs.objects.get(pk=id)
#     context = {
#         'pas_chjs': pas_chjs,
#         'id_pas': id_pas,
#         #'pas_all': pas_all,
#     }
#     if request.method == 'POST':
#         form = PasFormEdit(request.POST)
#         if form.is_valid():
#             Pas_chjs.objects.create(**form.cleaned_data)
#             print(form.cleaned_data)
#             return redirect('main')
#     else:
#         form = PasFormEdit()
#     return render(request, 'pas_chjs/edit_pas.html', {'form': form, 'pas_chjs': pas_chjs, })

# Редактривание паспорта через форму
def edit_pas(request, id):
    pas_id = Pas_chjs.objects.get(pk=id)
    form = EditPasForm(request.POST or None, instance=pas_id)
    context = { 'form': form, }
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main')
    return render(request, 'pas_chjs/edit_pas.html', context)

# Добавление нового паспорта обьекта через свою форму
def add_pas(request):
    test = Pas_chjs.objects.aggregate(Max('pas_number'))
    max_pas = test['pas_number__max']
    if request.method == 'POST':
        form = PasForm(request.POST)
        if form.is_valid():
            Pas_chjs.objects.create(**form.cleaned_data)
            return redirect('main')
            #print(form.cleaned_data)
    else:
        form = PasForm()
    return render(request, 'pas_chjs/add_pas.html', {'form': form, 'max_pas': max_pas,})

# Добавление микрорайона через свою форму
def add_mkr(request):
    if request.method == 'POST':
        form = MkrForm(request.POST)
        if form.is_valid():
            #Mkr_name.objects.create(**form.cleaned_data)
            form.save()
            return redirect('main')
    else:
        form = MkrForm()
    return render(request, 'pas_chjs/add_mkr.html', {'form': form})

# Редактирование существущего микрорайона
def edit_mkr(request, id):
    mkr_id = Mkr_name.objects.get(pk=id)
    form = MkrForm(request.POST or None, instance=mkr_id)
    context = { 'form': form, }
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('main')
    return render(request, 'pas_chjs/edit_mkr.html', context)

# Добавление материала через свою форму
def add_materials_walls(request):
    if request.method == 'POST':
        form = MaterialsWallsForm(request.POST)
        if form.is_valid():
            #Mkr_name.objects.create(**form.cleaned_data)
            form.save()
            return redirect('main')
    else:
        form = MaterialsWallsForm()
    return render(request, 'pas_chjs/add_materials_walls.html', {'form': form})


def add_type_heat(request):
    if request.method == 'POST':
        form = TypeHeatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = TypeHeatForm()
    return render(request, 'pas_chjs/add_type_heat.html', {'form': form})


class Search(ListView):
    template_name = 'pas_chjs/search.html'
    context_object_name = 'pas_chjs'
    paginate_by = 1000

    def get_queryset(self):
        return Pas_chjs.objects.filter(pas_adress__icontains=self.request.GET.get('s'),)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context










































