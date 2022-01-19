from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import viewsets
from APPLICATION.models import Reponse
from rest_framework.permissions import IsAuthenticated
from user_management.serealize import Userserializer

# Create your views here


class MoiviewSet(viewsets.ViewSet):

    Permission_classes= (IsAuthenticated, )

    def list(self, request):

        user= User.objects.get(pk=request.user) 
        user_data = Userserializer(user).data
        return Reponse(user_data)