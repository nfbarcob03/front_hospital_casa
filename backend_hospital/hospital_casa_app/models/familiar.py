from django.db import models
from .user import User

class Familiar(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario = models.ForeignKey(User, related_name='usuario_familiar', on_delete=models.CASCADE, unique=True, null=True, blank=True)
    create_date = models.DateField('create_date')
    id_registra = models.IntegerField('id_registra', null=True, blank=True)