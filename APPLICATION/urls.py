from django.urls import path
from .import views
from .views import *
urlpatterns = [
    path('etudiants', StudentList.as_view()),
     path('requetes', RequestList.as_view()),
    path('administrations', AdministrateList.as_view()),
   

]
