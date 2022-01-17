from django.urls import path
from .import views
from .views import *
urlpatterns = [
    path('etudiants', StudentList.as_view()),
    path('requetes', RequestList.as_view()),
    path('envoyées', EnvoitList.as_view()),
    path('etudiant/<str:matricule>', views.getEtudiant),
    path('administration/<str:email_pass>', views.getAdministration),
    #path('etudiants/', views.allEtudiant),
    path('addetudiants/', views.addEtudiant),
    path('administration/', views.allAdministration),
    path('addadministration/', views.addAdministration),
    path('insert/user/', views.insertUser)
]
