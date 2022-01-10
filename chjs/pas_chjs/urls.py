from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('mkr_name/<int:mkr_name_pas_id>/', get_mkr_name, name='mkr'),
    path('pas/<int:id>/', get_pas, name='pas'), # заполнение шаблона бланка конкретным обьектом ЧЖС
    path('edit-pas/<int:id>/', edit_pas, name='edit-pas'),
    path('pas/add-pas/', add_pas, name='add_pas'),
    path('mkr/add-mkr/', add_mkr, name='add-mkr'),
    path('edit-mkr/<int:id>/', edit_mkr, name='edit-mkr'),
    path('search/', Search.as_view(), name='search'),
]