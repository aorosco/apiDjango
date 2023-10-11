from rest_framework import serializers
from .models import Docente, Periodo, Asignatura, Horario, HoraTemporada

class DocenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Docente
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Periodo
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asignatura
        fields = '__all__'

class HorarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horario
        fields = '__all__'

class HoraTemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = HoraTemporada
        fields = '__all__'
