from django.shortcuts import render, redirect
from django.db.models import *
from django.http import HttpResponse
from .forms import PasForm
from django.views.generic import ListView

from .models import *

def index(request):
    pas_chjs = Pas_chjs.objects.all()
    mkr_name = Mkr_name.objects.all()
    materials_walls = Materials_walls.objects.all()
    context = {
        'pas_chjs': pas_chjs,
        'title': 'Список паспортов ЧЖС',
        'mkr_name': mkr_name,
        'materials_wals': materials_walls,
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
    #pas_all = Pas_chjs.objects.all()
    id_pas = Pas_chjs.objects.get(pk=id)
    context = {
        'pas_chjs': pas_chjs,
        'id_pas': id_pas,
        #'pas_all': pas_all,
    }
    return render(request, 'pas_chjs/blank_chjs.html', context)

def add_pas(request):
    test = Pas_chjs.objects.aggregate(Max('pas_number'))
    max_pas = test['pas_number__max']
    print(test['pas_number__max'])
    if request.method == 'POST':
        form = PasForm(request.POST)
        if form.is_valid():
            Pas_chjs.objects.create(**form.cleaned_data)
            return redirect('main')
            #print(form.cleaned_data)
    else:
        form = PasForm()
    return render(request, 'pas_chjs/add_pas.html', {'form': form, 'max_pas': max_pas,})

class Search(ListView):
    template_name = 'pas_chjs/search.html'
    context_object_name = 'pas_chjs'
    paginate_by = 10000

    def get_queryset(self):
        return Pas_chjs.objects.filter(pas_adress__icontains=self.request.GET.get('s'),)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context)
        context['s'] = f"s={self.request.GET.get('s')}&"
        return context










































