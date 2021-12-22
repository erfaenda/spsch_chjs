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
