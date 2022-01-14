from django.db import models

# Create your models here.
from django.db import models
from django.db.models.fields.related import ForeignKey

class Utilisateur(models.Model):
    nom_prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Etudiant(Utilisateur):
    matricule = models.CharField( primary_key=True, max_length=8)
    filiere = models.CharField(max_length=20)
    niveau = models.CharField(max_length=10)

    def meStocker(self):
        etudiant = Etudiant(matricule = self.matricule, nom_prenom = self.nom_prenom, email = self.email, password = self.password, filiere = self.filiere, niveau = self.niveau)
        etudiant.save()


class Grade(models.Model):
    nom_grade = models.CharField(primary_key=True, max_length=10 )
    pass

    
class Administration(Utilisateur):
    email_pass = models.CharField(primary_key=True, max_length=30 )
    departement = models.CharField(max_length=15)
    grade = models.ForeignKey( Grade, on_delete=models.CASCADE)



class Requete(models.Model):
    description = models.TextField()
    id_request = models.AutoField(auto_created=True, primary_key=True)

    

class Demande(Requete):
    object_demande= models.TextField()
    

class Abscence_note(Requete):
    unite_enseignement= models.CharField( max_length=7)
    examen= models.CharField(max_length=10)
   
class Activation_de_matricule(Requete):
    matricule_etudiant= models.CharField(max_length=10)


class Abscence_payement(Requete):
    matricule_etudiant= models.CharField(max_length=10)

class PieceJointe(models.Model):
    requete= models.ForeignKey(Requete, on_delete=models.CASCADE)
    nom_piece= models.CharField(max_length=50)
    type_piece=models.CharField(max_length=10)


class Envoyer (models.Model):
    administration= models.ForeignKey(Administration, on_delete=models.CASCADE)
    etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    requete= models.ForeignKey(Requete, on_delete=models.CASCADE)
    dateHeureEnvoie = models.DateTimeField()

class Reponse (models.Model):
    id_reponse = models.AutoField(primary_key=True, auto_created=True)
    requete= models.ForeignKey(Requete, on_delete=models.CASCADE)
    dateHeureRep = models.DateTimeField()
    status = models.CharField(max_length=30)
    description = models.TextField(max_length=15)


class Bloquage_matricule(Requete):
    matricule_etudiant=models.CharField(max_length=10)

class Changement_filiere(Requete):
    anciene_filiere= models.CharField(max_length=50)
    new_filiere= models.CharField(max_length=50)

class Note_erronee(Requete):

    note_errone= models.FloatField()
    note_correct= models.FloatField()
    examen=models.CharField(max_length=30)
    unite_enseignement=models.CharField(max_length=30)


class Information_eronee(Requete):
    non_erronee= models.CharField(max_length=100)
    matricule_erronee= models.CharField(max_length=7)
    non_correct= models.CharField(max_length=100)
    matricule_correct= models.CharField(max_length=7)