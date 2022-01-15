from rest_framework import serializers
from.models import*


""" """
class AdministrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administration
        fields = '__all__'

class EtudiantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'




class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = '__all__'

class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'

class EnvoyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Envoyer
        fields = '__all__'

class DemandeSerialize(serializers.ModelSerializer):
    class Meta:
        model = Demande
        fields = '_all_'

class Abscence_noteSerialize(serializers.ModelSerializer):
    class Meta:
        model = Abscence_note
        fields = '_all_'


class Activation_de_matriculeSerialize(serializers.ModelSerializer):
    class Meta:
        model = Activation_de_matricule
        fields = '_all'

class Abscence_payementSerialize(serializers.ModelSerializer):
    class Meta:
        model = Abscence_payement
        fields = '_all'


class PieceJointeSerialize(serializers.ModelSerializer):
    class Meta:
        model = PieceJointe
        fields = '_all'

class Bloquage_matriculeSerialize(serializers.ModelSerializer):
    class Meta:
        model = Bloquage_matricule
        fields = '_all'


class Changement_filiereSerialize(serializers.ModelSerializer):
    class Meta:
        model = Changement_filiere
        fields = '_all'


class Note_erroneeSerialize(serializers.ModelSerializer):
    class Meta:
        model = Note_erronee
        fields = '_all'

class Information_eroneeSerialize(serializers.ModelSerializer):
    class Meta:
        model = Information_eronee
        fields = '_all'