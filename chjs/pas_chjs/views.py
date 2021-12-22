from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def index(request):
    pas_chjs = Pas_chjs.objects.all()
    context = {
        'pas_chjs': pas_chjs,
        'title': 'Список паспортов ЧЖС'
    }
    return render(request, 'pas_chjs/index.html', context)
