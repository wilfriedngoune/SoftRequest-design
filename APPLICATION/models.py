from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models
from django.db.models.fields.related import ForeignKey


class Preference(models.Model):
    langue = models.CharField(max_length=30, null=True)
    theme = models.CharField(max_length=30, null=True)
    couleur_avartar = models.CharField(max_length=30, null=True)


class Administration(models.Model):
   
    GRADES = [('Chargé de cours', 'Chargé de cours'),
                ('Enseignant', 'Enseignant'), ('Doctorant', 'Doctorant'),
                ('Doyen', 'Doyen'),('Vice_Doyen', 'Vice_Doyen'),('Recteur', 'Recteur')]

    user = models.OneToOneField(User,  on_delete=models.CASCADE )
    id_Admin = models.CharField(unique = True, max_length=30, null=False)
    departement = models.CharField(max_length=30)
    grade = models.CharField(max_length=100, choices = GRADES)
    preference = models.OneToOneField (Preference, on_delete= models.CASCADE, null = True)


class Etudiant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    matricule = models.CharField( unique=True, max_length=8)
    filiere = models.CharField(max_length=20)
    niveau = models.CharField(max_length=20)
    preference = models.OneToOneField (Preference, on_delete= models.CASCADE , null = True)


"""class Requete(models.Model):
    objet = models.CharField(max_length= 100)
    description = models.TextField( null = True)
    Type = models.CharField(max_length= 100)"""


class Reponse(models.Model):
    dateHeureRep = models.DateTimeField()
    status = models.CharField(max_length=30)
    description = models.TextField(null = True, blank=True)


class Requete_personalisee(models.Model):
    objet = models.CharField(max_length= 100)
    description = models.TextField(blank=True, null = True)
    date =  models.DateTimeField(auto_now=True)
    Administration = models.ForeignKey(Administration, on_delete=models.DO_NOTHING)
    Etudiant = models.ForeignKey(Etudiant, on_delete=models.DO_NOTHING)
    reponse = models.ForeignKey(Reponse, on_delete=models.DO_NOTHING)


class ReqDemande(models.Model):
    objet = models.CharField(max_length= 100)
    description = models.TextField(blank=True, null = True)
    date =  models.DateTimeField(auto_now=True)
    nomDocument = models.CharField(max_length=20)
    anneeAcademique = models.CharField(max_length=10)
    Administration = models.ForeignKey(Administration, on_delete=models.DO_NOTHING)
    Etudiant = models.ForeignKey(Etudiant, on_delete=models.DO_NOTHING)
    reponse = models.ForeignKey(Reponse, on_delete=models.DO_NOTHING)


class ReqAbsence(models.Model):
    objet = models.CharField(max_length= 100)
    description = models.TextField(blank=True, null = True)
    date =  models.DateTimeField(auto_now=True)
    unite_enseignement= models.CharField( max_length=30)
    examen= models.CharField(max_length=30)
    Administration = models.ForeignKey(Administration, on_delete=models.DO_NOTHING)
    Etudiant = models.ForeignKey(Etudiant, on_delete=models.DO_NOTHING)
    reponse = models.ForeignKey(Reponse, on_delete=models.DO_NOTHING)


class ReqInformation_eronee(models.Model):
    objet = models.CharField(max_length= 100)
    description = models.TextField(blank=True, null = True)
    date =  models.DateTimeField(auto_now=True)
    ancienneInfo= models.CharField(max_length=50)
    nouvelleInfo= models.CharField(max_length=50)
    administration = models.ForeignKey(Administration, on_delete=models.DO_NOTHING)
    etudiant = models.ForeignKey(Etudiant, on_delete=models.DO_NOTHING)
    reponse = models.ForeignKey(Reponse, on_delete=models.DO_NOTHING)


class PieceJointe(models.Model):
    req_inf= models.ForeignKey(ReqInformation_eronee, on_delete=models.CASCADE)
    req_perso= models.ForeignKey(Requete_personalisee, on_delete=models.CASCADE)
    req_abs= models.ForeignKey(ReqAbsence, on_delete=models.CASCADE)
    req_dem = models.ForeignKey(ReqDemande, on_delete=models.DO_NOTHING)
    nom_pieceJointe= models.CharField(max_length=50)
    type_pieceJointe=models.CharField(max_length=10)
    pieceJointe = models.FileField(upload_to= 'Pieces')
 

"""class Envoyer (models.Model):
    id_envoi = models.CharField(unique=True, max_length=20, null=True)
    administration= models.ForeignKey(Administration, on_delete=models.CASCADE)
    etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    requete= models.ForeignKey(Requete, on_delete=models.CASCADE)
    dateHeureEnvoie = models.DateTimeField()"""



