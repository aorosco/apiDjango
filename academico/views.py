'''from django.shortcuts import render'''

from rest_framework import viewsets
from .models import Docente, Periodo, Asignatura, Horario, HoraTemporada
from .serializers import DocenteSerializer, PeriodoSerializer, AsignaturaSerializer, HorarioSerializer, HoraTemporadaSerializer

class DocenteViewSet(viewsets.ModelViewSet):
    queryset = Docente.objects.all()
    serializer_class = DocenteSerializer

class PeriodoAcademicoViewSet(viewsets.ModelViewSet):
    queryset = Periodo.objects.all()
    serializer_class = PeriodoSerializer

class AsignaturaViewSet(viewsets.ModelViewSet):
    queryset = Asignatura.objects.all()
    serializer_class = AsignaturaSerializer

class HorarioViewSet(viewsets.ModelViewSet):
    queryset = Horario.objects.all()
    serializer_class = HorarioSerializer

class HoraTemporadaViewSet(viewsets.ModelViewSet):
    queryset = HoraTemporada.objects.all()
    serializer_class = HoraTemporadaSerializer
