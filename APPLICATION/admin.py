from django.contrib import admin
from .models import*

# Register your models here.

admin.site.register(Administration)
admin.site.register(Etudiant)
admin.site.register(Grade)
admin.site.register(Requete)
admin.site.register(Abscence_note)
admin.site.register(Abscence_payement)
admin.site.register(Activation_de_matricule)
admin.site.register(Demande)
admin.site.register( PieceJointe)
admin.site.register(Reponse)
admin.site.register(Envoyer)
admin.site.register(Bloquage_matricule)
admin.site.register(Changement_filiere)
admin.site.register(Information_eronee)
admin.site.register(Note_erronee)