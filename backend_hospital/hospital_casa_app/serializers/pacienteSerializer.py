from hospital_casa_app.models.paciente import Paciente
from hospital_casa_app.models.user import User
from rest_framework import serializers
from datetime import datetime
from hospital_casa_app.serializers.userSerializer import UserSerializer
""
class PacienteSerializer(serializers.ModelSerializer):
    ##user = UserSerializer()
    class Meta:
        model = Paciente
        fields = ['id', 'eps', 'id_registra', 'usuario', 'create_date']

    def create(self, validated_data):
        pacienteInstance = Paciente.objects.create(**validated_data)
        return pacienteInstance

    
    def to_representation(self, obj):
        paciente = Paciente.objects.get(id=obj.id)
        user = User.objects.get(id=paciente.usuario.id)
        
        return {
        'paciente':{
            'id_paciente': paciente.id,
            'create_date_páciente':paciente.create_date,
            'eps': paciente.eps,
            'id_registra_paciente': paciente.id_registra,
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