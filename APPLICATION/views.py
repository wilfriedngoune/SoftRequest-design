from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin, DestroyModelMixin)
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.serializers import Serializer
from rest_framework import status
from .serializers import*
from .models import* 
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponseRedirect, request, response
from django.shortcuts import render
from .forms import *
from drf_yasg.utils import swagger_auto_schema

from rest_framework.decorators import action


# Create your views here.

class UserList(CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

   
class StudentList(CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = EtudiantSerializer
    queryset = Etudiant.objects.all()


class Administration(CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = AdministrationSerializer
    queryset = Administration.objects.all()


class ReqPersonaliseeViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = ReqPersonaliseSerializer
    queryset = ReqPersonalisee.objects.all()


class ReqInformation_eroneeViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = ReqInformation_eroneeSerializer
    queryset = ReqInformation_eronee.objects.all()


class ReqAbsenceViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = ReqAbsenceSerializer
    queryset = ReqAbsence.objects.all()

class ReqDemandeViewSet(CreateModelMixin, ListModelMixin, RetrieveModelMixin,UpdateModelMixin, DestroyModelMixin, GenericViewSet):
    serializer_class = ReqDemandeSerializer
    queryset = ReqDemande.objects.all()



class SignIn(GenericViewSet):

    serializer_class = SignInSerializer

    @swagger_auto_schema(
        request_body = SignInSerializer, 
        operation_description = " Test l'authenticité des infos entrées et retourne le token s'ils sont valident"
    )
    @action(methods=['POST'], detail=False)

    def signin(self, request, *args, **kwargs):
        userserialize = SignInSerializer(data = self.request.data)
        userserialize.is_valid(raise_exception=True)

        username = userserialize.validated_data.get("username")
        password = userserialize.validated_data.get("password")

        user = authenticate(username=username, password=password)

        if user is not None :
            if user.is_active:
                login(request, user)
                token = Token.objects.get_or_create(user)[0].key
                users = UserSerializer(user).data
                return Response({'user': users }, status=status.HTTP_200_OK)
            else:
                return Response({"message" : "non autorisé, utilisateur / mot de passe incorrect"}, status = status.HTTP_401_UNAUTHORIZED) 
        else:
                return Response({"message" : "non autorisé, utilisateur / mot de passe incorrect"}, status = status.HTTP_401_UNAUTHORIZED)



class SignOut(GenericViewSet):

    @swagger_auto_schema(
        operation_description = " Test l'authenticité des infos entrées et retourne le token s'ils sont valident"
    )
    @action(methods=['POST'], detail=False)

    def signout(self, request, *args, **kwargs):
        user = request.user.username
        request.user.auth_token.delete()
        logout(request)
        
        return Response({"message" : f"Hasta la proxima ves!!{user}"}, status = status.HTTP_200_OK)

