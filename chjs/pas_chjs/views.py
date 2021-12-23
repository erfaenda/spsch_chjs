from django.shortcuts import render
from django.http import HttpResponse

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








































