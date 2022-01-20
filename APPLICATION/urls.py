from venv import create
from django.urls import re_path
from django.urls import path
from .import views
from .views import *
urlpatterns = [
    re_path('insert/user/', views.insertUser),
    path('etudiants/', StudentList.as_view({'get':'list','post':'create'})),
    path('user/', UserList.as_view({'get':'list','post':'create'})),
    path('administration/', AdministrationList.as_view({'get':'list','post':'create'})),
    path('etudiant/<str:matricule>', views.getEtudiant),
    path('administration/<str:email_pass>', views.getAdministration),
    #path('etudiants/', views.allEtudiant),
    path('addetudiants/', views.addEtudiant),
    path('administrations/', views.allAdministration),
    path('addadministration/', views.addAdministration),


    #Mes trucs de test (ca va marcher, jai confiance)


]
