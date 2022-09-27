from rest_framework import status, views
from django.conf import settings
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from hospital_casa_app.models import User
from hospital_casa_app.serializers import AuxiliarSerializer
from rest_framework_simplejwt.backends import TokenBackend
from hospital_casa_app.serializers import UserSerializer
from  datetime import datetime

class CrearAuxiliarView(views.APIView):
    def post(self, request, *args, **kwargs):

        ##token = request.META.get('HTTP_AUTHORIZATION')[7:]
        ##tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        ##valid_data = tokenBackend.decode(token,verify=False)
        ##aux_registra = Auxiliar.objects.get(id=request.data['id_registra'])
        ##if valid_data['user_id'] != request.data['id_registra'] | aux_registra == None: 
        ##    stringResponse = {'detail':'Unauthorized Request'}
        ##    return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)


        ## Creacion usuario
        data_usuario= request.data.pop('usuario_info')
        now = datetime.now() # current date and time
        data_usuario['create_date'] = now.strftime("%Y-%m-%d")
        data_usuario['rol'] = User.AplicationRol.AUX
        serializer_user = UserSerializer(data=data_usuario)
        serializer_user.is_valid(raise_exception=True)
        usuario = serializer_user.save()

        #creacion auxiliar
        data_auxiliar = request.data.pop('auxiliar_info')
        data_auxiliar['usuario'] = usuario.id
        data_auxiliar['create_date'] = create_date=now.strftime("%Y-%m-%d")
        serializador_auxiliar = AuxiliarSerializer(data=data_auxiliar)
        serializador_auxiliar.is_valid(raise_exception=True)
        auxiliar = serializador_auxiliar.save()
        
        tokenData = {"username":data_usuario['username'],
        "password":data_usuario['password']}
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return_data = {"auxiliar":AuxiliarSerializer(auxiliar).data, 
        "token_data":tokenSerializer.validated_data}
        return Response(return_data, status=status.HTTP_201_CREATED)