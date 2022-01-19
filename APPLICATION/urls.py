from django.urls import path
from .import views
from .views import *
urlpatterns = [
    path('etudiants', StudentList.as_view()),
    path('requetes', RequestList.as_view()),
    path('administration', AdministrateList.as_view()),
    path('user', UserList.as_view()),
    
     

]
