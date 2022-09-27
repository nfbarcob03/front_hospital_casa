from django.db import models
from .user import User

class Paciente(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='usuario_paciente', on_delete=models.CASCADE, unique=True, null=True, blank=True)
    eps = models.CharField('eps', max_length = 15)
    create_date = models.DateField('create_date',null=True,)
    id_registra = models.IntegerField('id_registra', null=True, blank=True)