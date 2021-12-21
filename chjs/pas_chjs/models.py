from django.db import models

class Pas_chjs(models.Model):
     pas_number = models.IntegerField()
     mkr_name_pas = models.ForeignKey('Mkr_name', on_delete=models.PROTECT, null=True, verbose_name='Микрорайон')
     pas_adress = models.CharField(max_length=350)
     stages = models.IntegerField(blank=True)
     walls_material = models.ForeignKey('Materials_walls', on_delete=models.PROTECT, null=True, verbose_name='Стены', blank=True)
     electric = models.BooleanField(default=True)
     apis = models.IntegerField(blank=True)
     living = models.IntegerField(blank=True)
     childrens = models.IntegerField(blank=True)
     characteristic = models.TextField(blank=True)
     owner_name = models.CharField(max_length=200, blank=True)
     date_owner = models.DateField()
     woker_mchs = models.CharField(max_length=200)
     woker_date = models.DateField()
     unfineshed = models.BooleanField(default=False)
     created_at = models.DateTimeField(auto_now_add=True)
     created_update = models.DateTimeField(auto_now=True)


     def __int__(self):
         return self.pas_number

class Mkr_name(models.Model):
     name = models.CharField(max_length=150, db_index=True, verbose_name='Микрорайон')
     def __str__(self):
         return self.name

class Materials_walls(models.Model):
     name = models.CharField(max_length=150, db_index=True, verbose_name='Стены')
     def __str__(self):
          return self.name
