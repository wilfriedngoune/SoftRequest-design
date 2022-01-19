from dataclasses import field
from re import M
from tkinter import E
from rest_framework import serializers
from django.db import models
from django.contrib.auth.models import User
from.models import*


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')

class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('nom_grade')

class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        user = UserSerializer()
        model = Administration
        fields = ('user','id_Admin','departement','grade')

class EtudiantSerializer(serializers.ModelSerializer):
    
    user = UserSerializer()

    class Meta:
        model = Etudiant
        fields = ('user', 'matricule','filiere','niveau')

    def create(self, validated_data):

        user_info = self.validated_data.pop('user')
        first_name = user_info['first_name']
        last_name = user_info['last_name']
        email = user_info['email']
        password = user_info['password']
        username = user_info['username']
        user = User.objects.create(username = username, first_name = first_name, last_name = last_name,
                                         email = email, password = password)
        return Etudiant.objects.create(user = user, matricule = self.validated_data['matricule'],
                        filiere = self.validated_data['filiere'], niveau = self.validated_data['niveau'])       

class RequeteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requete
        fields = ('id_request','objet','description')


class PieceJointeSerialize(serializers.ModelSerializer):
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

class EnvoyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envoyer
        fields = ('id_envoi','administration','etudiant','requete','dateHeureEnvoie')


