from rest_framework import status, views
from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospital_casa_app.models.auxiliar import Auxiliar
from hospital_casa_app.serializers import PacienteSerializer
from rest_framework_simplejwt.backends import TokenBackend
from hospital_casa_app.serializers import UserSerializer
from hospital_casa_app.models import User
from hospital_casa_app.models import Paciente
from  datetime import datetime
from rest_framework.permissions import IsAuthenticated

def validateTokenAuxBody(request):
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token,verify=False)
    aux_registra = Auxiliar.objects.get(id=request.data['paciente_info']['id_registra'])
    tokenNoValido =  aux_registra == None  or valid_data['user_id'] != aux_registra.usuario.id 
    return tokenNoValido


def validateTokenAuxUrl(request, **kwargs):
    token = request.META.get('HTTP_AUTHORIZATION')[7:]
    tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
    valid_data = tokenBackend.decode(token,verify=False)
    aux_registra = Auxiliar.objects.get(id=kwargs['id_aux'])
    tokenNoValido = aux_registra == None  or valid_data['user_id'] != aux_registra.usuario.id
    return tokenNoValido


    

class PacienteView(views.APIView):
    def post(self, request, *args, **kwargs):
        tokenNoValido = validateTokenAuxBody(request)
        ##token = request.META.get('HTTP_AUTHORIZATION')[7:]
        #3tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        ##valid_data = tokenBackend.decode(token,verify=False)
        ##aux_registra = Auxiliar.objects.get(id=request.data['paciente_info']['id_registra'])
        if tokenNoValido: 
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

    def delete(self, request, *args, **kwargs):
        queryset = Paciente.objects.all()
        serializer_class = PacienteSerializer
        permission_classes = (IsAuthenticated,)

        tokenNoValido = validateTokenAuxUrl(request, **kwargs)
        if tokenNoValido: 
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        paciente= Paciente.objects.filter(id=kwargs['pk']).first()
        usuario = User.objects.filter(id = paciente.usuario.id).first()
        paciente.delete()
        usuario.delete()

        stringResponse = {'detail':'Registro eliminado'}
        return Response(stringResponse)
    
    def put(self, request, *args, **kwargs):

        permission_classes = (IsAuthenticated,)

        tokenNoValido = validateTokenAuxBody(request)
        if tokenNoValido: 
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        now = datetime.now() # current date and time

        #actualizacion paciente
        data_paciente = request.data.pop('paciente_info')
        data_paciente['create_date'] = create_date=now.strftime("%Y-%m-%d")
        paciente_actualizar = Paciente.objects.get(id=kwargs['pk'])

        serializer_paciente = PacienteSerializer(paciente_actualizar, data=data_paciente)
        serializer_paciente.is_valid(raise_exception=True)
        paciente = serializer_paciente.save()

        ## actualizacion usuario
        data_usuario= request.data.pop('usuario_info')
        data_usuario['create_date'] = create_date=now.strftime("%Y-%m-%d")
        usuario_actualizar = User.objects.get(id=paciente.usuario.id)
        serializer_user = UserSerializer(usuario_actualizar,data=data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save()
    
        return_data = {"paciente":PacienteSerializer(paciente).data}
        return Response(return_data, status=status.HTTP_201_CREATED)


        
    def get(self, request, *args, **kwargs):
        tokenNoValido = validateTokenAuxUrl(request, **kwargs)
        if tokenNoValido: 
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)

        paciente= Paciente.objects.filter(id=kwargs['pk']).first()
        serializer = PacienteSerializer(paciente)
        return Response(serializer.data)

    