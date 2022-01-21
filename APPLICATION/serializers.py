from dataclasses import field, fields
from re import M
from tkinter import E
from rest_framework import serializers, fields
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from.models import*


class UserSerializer(serializers.ModelSerializer):

    def update(self, instance:User, validated_data):
        validated_data.pop("password")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password')
        extra_kwargs = {"password" : {"write_only": True}}


class AdministrationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Administration.objects.create(**validated_data) 

    def update(self, instance:Administration, validated_data):
        validated_data.pop("user")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance
    
    class Meta:
        model = Administration
        fields = ('user', 'id', 'departement', 'grade')
    
          
class EtudiantSerializer(serializers.ModelSerializer):
        
    def create(self, validated_data):
        return Etudiant.objects.create(**validated_data)
                    
    def update(self, instance:Etudiant, validated_data):
        validated_data.pop("user")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = Etudiant
        fields = ('user', 'matricule','filiere','niveau')


class PieceJointeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return PieceJointe.objects.create(**validated_data)

    def update(self, instance:PieceJointe, validated_data):
        validated_data.pop("requete")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = PieceJointe
        fields = ('requete','nom_pieceJointe','type_pieceJointe','pieceJointe')


class ReqDemandeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ReqDemande.objects.create(**validated_data)

    def update(self, instance:ReqDemande, validated_data):
        validated_data.pop("administration")
        validated_data.pop("etudiant")
        validated_data.pop("reponse")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = ReqDemande
        fields = ('objet','description','date','nomDocument','anneeAcademique','administration','etudiant','reponse')



class ReqPersonaliseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ReqPersonalisee.objects.create(**validated_data)

    def update(self, instance:ReqPersonalisee, validated_data):
        validated_data.pop("administration")
        validated_data.pop("etudiant")
        validated_data.pop("reponse")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = ReqDemande
        fields = ('objet','description','date','administration','etudiant','reponse')




class ReqAbsenceSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ReqAbsence.objects.create(**validated_data)

    def update(self, instance:ReqAbsence, validated_data):
        validated_data.pop("administration")
        validated_data.pop("etudiant")
        validated_data.pop("reponse")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = ReqAbsence
        fields = ('objet','description','date','unite_enseignement','examen','administration','etudiant','reponse')


class ReqInformation_eroneeSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return ReqInformation_eronee.objects.create(**validated_data)

    def update(self, instance:ReqInformation_eronee, validated_data):
        validated_data.pop("administration")
        validated_data.pop("etudiant")
        validated_data.pop("reponse")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = ReqInformation_eronee
        fields = ('objet','description','date','ancienneInfo','nouvelleInfo','administration','etudiant','reponse')


class ReponseSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Reponse.objects.create(**validated_data)

    def update(self, instance:Reponse, validated_data):
        validated_data.pop("administration")
        validated_data.pop("etudiant")
        validated_data.pop("reponse")
        for key, value in validated_data.items():
            setattr(instance, key, value)
        return instance

    class Meta:
        model = Reponse
        fields = ('dateHeureRep','status','description')

class SignInSerializer(serializers.Serializer):
    username = fields.CharField(required= True)
    password = fields.CharField( write_only= True, required= True)
    token = fields.SerializerMethodField()

    def get_token(self, instance : User):
        return Token.object.get( user= instance).key

"""
class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = """