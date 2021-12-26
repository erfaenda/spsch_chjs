from django.shortcuts import render
from django.http import HttpResponse
from .forms import PasForm

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
    if request.method == 'POST':
        pass
    else:
        form = PasForm()
    return render(request, 'pas_chjs/add_pas.html', {'form': form})








































