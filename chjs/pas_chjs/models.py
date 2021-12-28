from django.db import models

class Pas_chjs(models.Model):
     pas_number = models.IntegerField(verbose_name='Номер паспорта', unique=True)
     mkr_name_pas = models.ForeignKey('Mkr_name', on_delete=models.PROTECT, null=True, verbose_name='Микрорайон')
     pas_adress = models.CharField(max_length=350, verbose_name='Адрес')
     stages = models.IntegerField(blank=True, verbose_name='Этажность')
     walls_material = models.ForeignKey('Materials_walls', on_delete=models.PROTECT, null=True, verbose_name='Стены', blank=True)
     type_heat = models.ForeignKey('Type_heat', on_delete=models.PROTECT, null=True, verbose_name='Вид отопления')
     electric = models.BooleanField(default=True, verbose_name='Электрофицирован')
     apis = models.IntegerField(default=0, verbose_name='АПИ', blank=True)
     apis_works = models.IntegerField(default=0, verbose_name='АПИ исправны', blank=True)
     living = models.IntegerField(default=0, verbose_name='Проживает', blank=True)
     childrens = models.IntegerField(default=0, verbose_name='Дети', blank=True)
     characteristic = models.TextField(blank=True, verbose_name='Характеристика')
     owner_name = models.CharField(max_length=200, blank=True, verbose_name='Имя собственника')
     date_owner = models.DateField(verbose_name='Дата', blank=True)
     woker_mchs = models.CharField(max_length=200, verbose_name='Сотрудник', blank=True)
     woker_date = models.DateField(verbose_name='Дата', blank=True)
     unfineshed = models.BooleanField(default=False, verbose_name='Недострой', blank=True)
     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано', blank=True)
     created_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено', blank=True)


     def __str__(self):
         #str_pas_number = str(self.pas_number)
         print(self.pas_adress)
         return self.pas_adress

     class Meta:
          verbose_name = 'Паспорт'
          verbose_name_plural = 'Паспорта'
          ordering = ['-created_at']

class Mkr_name(models.Model):
     name = models.CharField(max_length=150, db_index=True, verbose_name='Микрорайон')
     def __str__(self):
         return self.name

     class Meta:
          verbose_name = 'Микрорайон'
          verbose_name_plural = 'Микрорайоны'
          #ordering = ['created_at']

class Materials_walls(models.Model):
     name = models.CharField(max_length=150, db_index=True, verbose_name='Стены')
     def __str__(self):
          return self.name

     class Meta:
          verbose_name = 'Материал'
          verbose_name_plural = 'Материалы'
          #ordering = ['-created_at']

class Type_heat(models.Model):
     name = models.CharField(max_length=150, db_index=True, verbose_name='Вид отопления')
     def __str__(self):
          return self.name

     class Meta:
          verbose_name = 'Вид отопления'
          verbose_name_plural = 'Виды отопления'
          #ordering = ['-created_at']
