from django.shortcuts import render
from rest_framework.decorators import api_view
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
class StudentList(generics.ListCreateAPIView):
    queryset = Etudiant.objects.all()
    serializer_class = EtudiantSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EtudiantSerializer(queryset, many = True)
        return Response(serializer.data)

#Endpoint qui permet de mettre un etudiant dans la base de donne
class RequestList(generics.ListCreateAPIView):
    queryset = Requete.objects.all()
    serializer_class = RequeteSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = RequeteSerializer(queryset, many = True)
        return Response(serializer.data)




#Endpoint qui permet de mettre un administration dans la base de donne
class AdministrateList(generics.ListCreateAPIView):
    queryset = Administration.objects.all()
    serializer_class = AdministrationSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = AdministrationSerializer(queryset, many = True)
        return Response(serializer.data)



"""
@api_view(['POST'])
def insertUser(request):
    if request.method == 'POST':
        etudiant_data=JSONParser().parse(request)
        etudiants_serializer=EtudiantSerializer(data=etudiant_data)
        if etudiants_serializer.is_valid():
            etudiants_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)




@api_view(['GET'])
    E1 = Etudiant()
    E1.meStocker()
    etudiants = Etudiant.objects.all()
    serialization = EtudiantSerializer(etudiants, many = True)
    return Response(serialization.data)












Api pour  afficher tous les etudiants et enseignants
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

@csrf_exempt
def etudiantApi(request,id= ""):
    if request.method=='GET':
        etudiants = Etudiant.objects.all()
        etudiants_serializer=EtudiantSerializer(etudiants,many=True)
        return JsonResponse(etudiants_serializer.data,safe=False)
    elif request.method=='POST':
        etudiant_data=JSONParser().parse(request)
        etudiants_serializer=EtudiantSerializer(data=etudiant_data)
        if etudiants_serializer.is_valid():
            etudiants_serializer.save()
            return JsonResponse("Added Successfully",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        etudiant_data=JSONParser().parse(request)
        etudiant=Etudiant.objects.get(matricule=etudiant_data['matricule'])
        etudiants_serializer=EtudiantSerializer(etudiant,data=etudiant_data)
        if etudiants_serializer.is_valid():
            etudiants_serializer.save()
            return JsonResponse("Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method=='DELETE':
        etudiant=Etudiant.objects.get(matricule=id)
        etudiant.delete()
        return JsonResponse("Deleted Successfully",safe=False)
"""