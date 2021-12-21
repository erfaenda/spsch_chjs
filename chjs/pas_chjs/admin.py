from django.contrib import admin
from .models import *

'''class Mkr_name_admin(admin.ModelAdmin):
    list_display = ('id', 'mkr_name_pas')
    list_display_links = ('id', 'mkr_name_pas')
    search_fields = ('mkr_name_pas',)'''

#регестрация приложений в даминке
admin.site.register(Mkr_name)
admin.site.register(Materials_walls)
admin.site.register(Pas_chjs)
