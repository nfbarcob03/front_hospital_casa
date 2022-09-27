from rest_framework import serializers
from hospital_casa_app.models import User
from hospital_casa_app.models import Paciente


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password','activo', 'nombre', 'apellido', 'correo', 'direccion', 'telefono','rol', 'create_date']

        def create(self, validated_data):
            userInstance = User.objects.create( **validated_data)
            return userInstance