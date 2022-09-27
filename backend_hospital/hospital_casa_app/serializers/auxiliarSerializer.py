from hospital_casa_app.models.user import User
from hospital_casa_app.models.auxiliar import Auxiliar
from rest_framework import serializers
from datetime import datetime
from hospital_casa_app.serializers.userSerializer import UserSerializer
""
class AuxiliarSerializer(serializers.ModelSerializer):
    ##user = UserSerializer()
    class Meta:
        model = Auxiliar
        fields = ['id', 'cargo', 'usuario', 'create_date']

    def create(self, validated_data):
        auxiliarInstance = Auxiliar.objects.create(**validated_data)
        return auxiliarInstance

    
    def to_representation(self, obj):
        auxiliar = Auxiliar.objects.get(id=obj.id)
        user = User.objects.get(id=auxiliar.usuario.id)
        
        return {
        'auxiliar':{
            'id_auxiliar': auxiliar.id,
            'create_date':auxiliar.create_date,
            'cargo': auxiliar.cargo,
            'id_registra_auxiliar': auxiliar.id_registra,
        },
        'usuario':{
            'id_usuario':user.id,
            'username': user.username,
            'nombre': user.nombre,
            'apellido': user.apellido,
            'create_date_user': user.create_date,
            'activo':user.activo,
            'correo': user.correo,
            'direccion': user.direccion,
            'telefono':user.telefono,
            'rol':user.rol
        }
    }