from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import*
from .models import* 

# Create your views here.

# Api pour  afficher tous les etudiants et enseignants
@api_view(['GET'])
def allEtudiant(request):
    etudiants = Etudiant.objects.all()
    serialization = EtudiantSerializer(etudiants, many = True)
    return Response(serialization.data)

@api_view(['GET'])
def allAdministration(request):
    administration = Etudiant.objects.all()
    serializer = EtudiantSerializer(administration, many = True)
    return Response(serializer.data)

# Api pour  afficher un etudiant/enseignant
@api_view(['GET'])
def getEtudiant(request):
    etudiant = Etudiant.objects.get (matricule = id)
    serialization = EtudiantSerializer(etudiant)
    return Response(serialization.data)

@api_view(['GET'])
def getAdministration(request):
    administration = Administration.objects.get (id = id)
    serialization = EtudiantSerializer(administration)
    return Response(serialization.data)



@api_view(['POST'])
def addEtudiant(request):
    
    serialization = EtudiantSerializer(data = request.data,many = True)
    if serialization.is_valid():
        serialization.save()
    return Response(serialization.data)

@api_view(['POST'])
def addAdministration(request):
    
    serializer = EtudiantSerializer(data = request.data,many = True)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)