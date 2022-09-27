from rest_framework import status, views
from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospital_casa_app.models.auxiliar import Auxiliar
from hospital_casa_app.serializers import PacienteSerializer
from rest_framework_simplejwt.backends import TokenBackend
from hospital_casa_app.serializers import UserSerializer
from hospital_casa_app.models import User
from  datetime import datetime

class CreatePacienteView(views.APIView):
    def post(self, request, *args, **kwargs):

        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data = tokenBackend.decode(token,verify=False)
        aux_registra = Auxiliar.objects.get(id=request.data['paciente_info']['id_registra'])
        if valid_data['user_id'] != aux_registra.usuario.id or aux_registra == None: 
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)


        ## Creacion usuario
        data_usuario= request.data.pop('usuario_info')
        now = datetime.now() # current date and time
        data_usuario['rol'] = User.AplicationRol.PAC
        data_usuario['create_date'] = create_date=now.strftime("%Y-%m-%d")
        serializer_user = UserSerializer(data=data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save()

        #creacion paciente
        data_paciente = request.data.pop('paciente_info')
        data_paciente['usuario'] = usuario.id
        data_paciente['create_date'] = create_date=now.strftime("%Y-%m-%d")
        serializer_paciente = PacienteSerializer(data=data_paciente)
        serializer_paciente.is_valid(raise_exception=True)
        paciente = serializer_paciente.save()
        
        tokenData = {"username":data_usuario['username'],
        "password":data_usuario['password']}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return_data = {"paciente":PacienteSerializer(paciente).data, 
        "token_data":tokenSerializer.validated_data}
        return Response(return_data, status=status.HTTP_201_CREATED)