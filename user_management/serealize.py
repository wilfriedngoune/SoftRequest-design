from django.contrib.auth.models import User
from rest_framework import serializers

class Userserializer(serializers.ModelSerializer):
    class meta:
        model= User
        field = '__all__'

