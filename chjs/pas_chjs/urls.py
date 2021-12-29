from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('mkr_name/<int:mkr_name_pas_id>/', get_mkr_name, name='mkr'),
    path('pas/<int:id>/', get_pas, name='pas'),
    path('pas/add-pas/', add_pas, name='add_pas'),
    path('search/', Search.as_view(), name='search'),
]