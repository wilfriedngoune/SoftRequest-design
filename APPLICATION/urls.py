from django.urls import path
from .import views

urlpatterns = [
    
    path('etudiant/<int:id>', views.getEtudiant),
    path('administration/<int:id>', views.getAdministration),
    path('etudiants/', views.allEtudiant),
    path('addetudiants/', views.addEtudiant),
    path('administration/', views.allAdministration),
    path('addadministration/', views.addAdministration)
]