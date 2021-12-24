from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('mkr_name/<int:mkr_name_pas_id>/', get_mkr_name),
    path('pas/<int:id>/', get_pas),
]