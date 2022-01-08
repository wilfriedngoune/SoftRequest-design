from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import*
from .models import* 

# Create your views here.
api_view(['Get'])

def