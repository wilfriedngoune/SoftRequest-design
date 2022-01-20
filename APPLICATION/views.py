from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, ListModelMixin)
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from rest_framework.serializers import Serializer
from .serializers import*
from .models import* 
#importation des fichier necessaire pour 
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import *




# Create your views here.


#Endpoint qui permet de mettre un etudiant dans la base de donne

class UserList(CreateModelMixin, ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


"""class StudentList(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = EtudiantSerializer
    queryset = Etudiant.objects.raw('SELECT * FROM APPLICATION_Etudiant WHERE matricule = "19M2325"')"""


class StudentList(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = EtudiantSerializer
    queryset = Etudiant.objects.all()


    """def list(self, request):
        queryset = self.get_queryset()
        serializer = EtudiantSerializer(queryset, many = True)
        return Response(serializer.da   ta)"""

class AdministrationList(CreateModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = AdministrationSerializer
    queryset = Administration.objects.all()



@api_view(['POST'])
def insertUser(request):
    if request.method == 'POST':
        etudiant_data = request.data
        etudiants_serializer = EtudiantSerializer(data=etudiant_data)
        if etudiants_serializer.is_valid():
            etudiants_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)






"""@api_view(['GET'])
    E1 = Etudiant()
    E1.meStocker()
    etudiants = Etudiant.objects.all()
    serialization = EtudiantSerializer(etudiants, many = True)
    return Response(serialization.data)"""











# Api pour  afficher tous les etudiants et enseignants
@api_view(['GET'])
def allEtudiant(request):
    etudiants = Etudiant.objects.all()
    serialization = EtudiantSerializer(etudiants, many = True)
    return Response(serialization.data)


@api_view(['GET'])
def allAdministration(request):
    administration = Administration.objects.all()
    serializer = AdministrationSerializer(administration, many = True)
    return Response(serializer.data)


# Api pour  creer  un etudiants et enseignants
@api_view(['POST'])
def addEtudiant(request):
    serialization = EtudiantSerializer(data = request.data,many = True)
    if serialization.is_valid():
        serialization.save()
    return Response(serialization.data)


@api_view(['POST'])
def addAdministration(request):
    
    serializer = AdministrationSerializer(data = request.data,many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



# Api pour  afficher un etudiant/enseignant
@api_view(['GET'])
def getEtudiant(request, matricule):
    etudiant = Etudiant.objects.get(matricule = matricule)
    serialization = EtudiantSerializer(etudiant)
    return Response(serialization.data)

@api_view(['GET'])
def getAdministration(request,email_pass):
    administration = Administration.objects.get (email_pass = email_pass)
    serialization = AdministrationSerializer(administration)
    return Response(serialization.data)

@api_view(['PUT'])
def updateAdministration(request,email_pass):
    administration = Administration.objects.get (email_pass = email_pass)
    serialization = AdministrationSerializer(instance= administration, data = request.data)
    if Serializer.is_valid():
        serialization.save()
    return Response(serialization.data)


@api_view(['PUT'])
def updateEtudiant(request,matricule):
    etudiants = Etudiant.objects.get (matricule = matricule)
    serialization = AdministrationSerializer(instance= etudiants, data = request.data)
    if Serializer.is_valid():
        serialization.save()
    return Response(serialization.data)


