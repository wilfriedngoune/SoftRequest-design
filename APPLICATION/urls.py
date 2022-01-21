from venv import create
from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import *

router = DefaultRouter()
router.register('user', UserList, basename= 'user')
router.register('admin', Administration, basename= 'admin')
router.register('etudiants', StudentList, basename= 'etudiant')
router.register('SignIn', SignIn, basename= 'SignIn')
router.register('SignOut', SignOut, basename= 'SignOut')
router.register('ReqAbsenceNote', ReqAbsenceViewSet, basename= 'ReqAbsenceNote')
router.register('ReqPersonnalisee', ReqPersonaliseeViewSet, basename= 'ReqPersonnalisee')
router.register('ReqDemande', ReqDemandeViewSet, basename= 'ReqDemande')
router.register('ReqInformation_erone', ReqInformation_eroneeViewSet, basename= 'ReqInformation_eronee')





urlpatterns = [
    path ('',include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace = 'rest_framework')),
    path('api-token-auth/', views.obtain_auth_token),

  
]
"""  path('user', UserList.as_view({'get':'list','post':'create'})),
    path('admin', Administration.as_view({'get':'list','post':'create'})),
    path('etudiants', StudentList.as_view({'get':'list','post':'create'})),
    path('etudiant/<str:matricule>', views.getEtudiant),
    path('administration/<str:email_pass>', views.getAdministration),
    #path('etudiants/', views.allEtudiant),
    path('addetudiants/', views.addEtudiant),
    path('administration/', views.allAdministration),
    path('addadministration/', views.addAdministration),
    path('insert/user/', views.insertUser)
    """
