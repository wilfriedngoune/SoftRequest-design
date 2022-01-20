from venv import create
from django.urls import re_path
from .import views
from .views import *
urlpatterns = [
    re_path('insert/user/', views.insertUser),
    re_path('etudiants/', StudentList.as_view({'get':'list','post':'create'})),
    re_path('user/', UserList.as_view({'get':'list','post':'create'})),
    re_path('administration/', AdministrationList.as_view({'get':'list','post':'create'})),
    re_path('etudiant/<str:matricule>', views.getEtudiant),
    re_path('administration/<str:email_pass>', views.getAdministration),
    #re_path('etudiants/', views.allEtudiant),
    re_path('addetudiants/', views.addEtudiant),
    re_path('administrations/', views.allAdministration),
    re_path('addadministration/', views.addAdministration),


    #Mes trucs de test (ca va marcher, jai confiance)


]
