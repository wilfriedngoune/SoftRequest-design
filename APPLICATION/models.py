from pyexpat import model
from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields.related import ForeignKey
from django.forms import CharField

# Create your models here.
#pour la realisation de notre bd nous allons  utiliser  le fichier model de notre  application


class Grade(models.Model):
    nom_grade = models.CharField(unique=True, max_length=10)

class Preference(models.Model):
    langue = models.CharField(max_length=30, null=True)
    theme = models.CharField(max_length=30, null=True)
    couleur_avartar = models.CharField(max_length=30, null=True)


class Administration(models.Model):
   
    user = models.OneToOneField(User,  on_delete=models.CASCADE )
    id_Admin = models.CharField(unique = True, max_length=30, null=False)
    departement = models.CharField(max_length=30)
    grade = models.ForeignKey( Grade, on_delete=models.CASCADE)
    #preference = models.OneToOneField (Preference, on_delete= models.CASCADE, null = True)

class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField( unique=True, max_length=8)
    filiere = models.CharField(max_length=20)
    niveau = models.CharField(max_length=20)
    #preference = models.OneToOneField (Preference, on_delete= models.CASCADE , null = True)


class Requete(models.Model):
    id_request = models.CharField(unique=True, max_length= 10, null=False)
    objet = models.CharField(max_length= 100)
    description = models.TextField( null = True)



class PieceJointe(models.Model):
    requete= models.ForeignKey(Requete, on_delete=models.CASCADE)
    nom_pieceJointe= models.CharField(max_length=50)
    type_pieceJointe=models.CharField(max_length=10)
    pieceJointe = models.FileField(upload_to= 'Pieces')
    

class ReqDemande(Requete):
    nomDocument = models.CharField(max_length=20)
    anneeAcademique = models.CharField(max_length=10)
    

class ReqAbsence(Requete):
    unite_enseignement= models.CharField( max_length=30)
    examen= models.CharField(max_length=30)

class ReqInformation_eronee(Requete):
    ancienneInfo= models.CharField(max_length=50)
    nouvelleInfo= models.CharField(max_length=50)
 

class Envoyer (models.Model):
    id_envoi = models.CharField(unique=True, max_length=20, null=True)
    administration= models.ForeignKey(Administration, on_delete=models.CASCADE)
    etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    requete= models.ForeignKey(Requete, on_delete=models.CASCADE)
    dateHeureEnvoie = models.DateTimeField()

class Reponse (models.Model):
    id_reponse = models.CharField(unique=True, max_length=20, null=False)
    administration= models.ForeignKey(Administration, on_delete=models.CASCADE)
    etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    requete= models.ForeignKey(Requete, on_delete=models.CASCADE)
    dateHeureRep = models.DateTimeField()
    status = models.CharField(max_length=30)
    description = models.TextField(null = True)


