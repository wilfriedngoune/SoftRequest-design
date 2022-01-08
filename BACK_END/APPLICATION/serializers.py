from rest_framework import serializers
from.models import*

""" classe"""
class Administration(serializers.ModelSerializer):
    class Meta:
        model: Administration
        fields = '__all__'

class Etudiant(serializers.ModelSerializer):
    class Meta:
        model: Etudiant
        fields = '__all__'

class Grade(serializers.ModelSerializer):
    class Meta:
        model: Grade
        fields = '__all__'

class Reponse(serializers.ModelSerializer):
    class Meta:
        model: Reponse
        fields = '__all__'

class Envoyer(serializers.ModelSerializer):
    class Meta:
        model: Envoyer
        fields = '__all__'

