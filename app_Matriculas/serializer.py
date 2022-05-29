# serializar es cambiar el fomri de salida de datos A json


__author__ = 'user'
from rest_framework import serializers
from .models import *

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'

class AlumnoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alumno
        fields = '__all__'
        