from django.db import models
from datetime import date

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name='Nombre * ')
    last_name = models.CharField(max_length=50, blank=True, default='', verbose_name='Apellido')
    phone = models.CharField(max_length=12, blank=True, default='', verbose_name='Teléfono')
    mobile = models.CharField(max_length=12, blank=False, verbose_name='Celular * ')
    email = models.EmailField(verbose_name='Email * ')
    company = models.CharField(max_length=30, blank=True, default='', verbose_name='Empresa')
    date = models.DateField(default=date.today)
    notes = models.TextField(blank=True, default='', verbose_name='Notas')

    def __str__(self):
        return "%s %s" % (self.name, self.last_name)
