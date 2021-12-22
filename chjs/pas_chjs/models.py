from django.db import models

class Pas_chjs(models.Model):
     pas_number = models.IntegerField(verbose_name='Номер паспорта', unique=True)
     mkr_name_pas = models.ForeignKey('Mkr_name', on_delete=models.PROTECT, null=True, verbose_name='Микрорайон')
     pas_adress = models.CharField(max_length=350, verbose_name='Адрес')
     stages = models.IntegerField(blank=True, verbose_name='Этажность')
     walls_material = models.ForeignKey('Materials_walls', on_delete=models.PROTECT, null=True, verbose_name='Стены', blank=True)
     electric = models.BooleanField(default=True, verbose_name='Электрофицирован')
     apis = models.IntegerField(default=0, verbose_name='АПИ')
     living = models.IntegerField(default=0, verbose_name='Проживает')
     childrens = models.IntegerField(default=0, verbose_name='Дети')
     characteristic = models.TextField(blank=True, verbose_name='Характеристика')
     owner_name = models.CharField(max_length=200, blank=True, verbose_name='Имя собственника')
     date_owner = models.DateField(verbose_name='Дата')
     woker_mchs = models.CharField(max_length=200, verbose_name='Сотрудник')
     woker_date = models.DateField(verbose_name='Дата')
     unfineshed = models.BooleanField(default=False, verbose_name='Недострой')
     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
     created_update = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

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
