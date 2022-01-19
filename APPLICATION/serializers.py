from dataclasses import fields
from rest_framework import serializers
from.models import*
from django.contrib.auth.models import User



# Create your models here.
#pour la realisation de notre bd nous allons  utiliser  le fichier model de notre  application
class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ('nom_grade')

class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = ('user','id_Admin','departement','grade')

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = ('user', 'matricule','filiere','niveau')


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

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= ('id', 'username', 'first_name', 'last_name', 'email')



