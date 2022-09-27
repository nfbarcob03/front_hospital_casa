from django.db import models
from .user import User
from .paciente import Paciente

class SignosVitales(models.Model):
    id = models.BigAutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, related_name='id_paciente', on_delete=models.CASCADE, null=True, blank=True)
    id_registra = models.IntegerField('id_registra', null=True, blank=True)
    saturacion = models.IntegerField('saturacion')
    presion = models.IntegerField('presion')
    frecuencia_cardiaca = models.IntegerField('frecuencia_cardiaca')
    create_date = models.DateField('create_date')
