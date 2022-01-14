from django.urls import path
from .import views

urlpatterns = [
    
    path('etudiant/<str:matricule>', views.getEtudiant),
    path('administration/<str:email_pass>', views.getAdministration),
    path('etudiants/', views.allEtudiant),
    path('addetudiants/', views.addEtudiant),
    path('administration/', views.allAdministration),
    path('addadministration/', views.addAdministration),
    path('insert/user/', views.insertUser)
]
