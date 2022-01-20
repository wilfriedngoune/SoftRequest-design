from dataclasses import field, fields
from re import M
from telnetlib import STATUS
from django.http import HttpResponse
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from.models import*


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')


class AdministrationSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()
    
    class Meta:
        model = Administration
        fields = ('user', 'id', 'departement', 'grade')
    
    def create(self, validated_data,):

        user_admin = self.validated_data.pop('user')
        username = user_admin['username']
        first_name = user_admin['first_name']
        last_name = user_admin['last_name']
        email = user_admin['email']
        password = user_admin['password']
        user = User.objects.create(username = username, first_name = first_name, last_name = last_name,
                                         email = email, password = password)
        return Administration.objects.create(user = user, grade = self.validated_data['grade'], departement = self.validated_data['departement'])       


class EtudiantSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Etudiant
        fields = ('user', 'matricule','filiere','niveau')

    def create(self, validated_data, request):
        user_info = self.validated_data.pop('user')
        first_name = user_info['first_name']
        last_name = user_info['last_name']
        email = user_info['email']
        password = user_info['password']
        user = User.objects.create(first_name = first_name, last_name = last_name,
                                         email = email, password = password)
        Etudiant.objects.create(user = user, matricule = self.validated_data['matricule'],
                      filiere = self.validated_data['filiere'], niveau = self.validated_data['niveau']) 
        return HttpResponse({
            'message' : 'Etudiant envoye avec succes ..'
        }, status = STATUS.HTTP_200_OK)     


class PieceJointeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PieceJointe
        fields = ('requete','nom_pieceJointe','type_pieceJointe','pieceJointe')


class ReqDemandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReqDemande
        fields = ('nomDocument','anneeAcademique')


class ReqAbsenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReqAbsence
        fields = ('unite_enseignement','examen')


class ReInformation_eroneeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReqInformation_eronee
        fields = ('info_erronee','ancienneInfo','nouvelleInfo')


class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = ('id_reponse','administration','etudiant','requete','dateHeureRep','status','description')

"""
class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = """