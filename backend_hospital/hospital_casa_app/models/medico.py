from django.db import models
from .user import User

class Medico(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='usuario_medico', on_delete=models.CASCADE, unique=True, null=True, blank=True)
    profesion =  models.CharField('profesion', max_length = 15)
    nivel = models.IntegerField('nivel', default=0)
    especialidad = models.CharField('especialidad', max_length = 15)
    create_date = models.DateField('create_date')
    id_registra = models.IntegerField('id_registra', null=True, blank=True)