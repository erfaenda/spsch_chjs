from django.contrib import admin
from .models import *

class Pas_chjs_admin(admin.ModelAdmin):
    list_display = ('pas_number', 'mkr_name_pas', 'pas_adress', 'created_at')
    list_display_links = ('mkr_name_pas', 'pas_adress')
    search_fields = ('pas_number', 'pas_adress')

#регестрация приложений в даминке
admin.site.register(Mkr_name)
admin.site.register(Materials_walls)
admin.site.register(Pas_chjs, Pas_chjs_admin)
admin.site.register(Type_heat)