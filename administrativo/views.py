from django.shortcuts import render

from rest_framework import viewsets
from .models import RegistroEntradaSalida
from .serializers import RegistroEntradaSalidaSerializer

class RegistroEntradaSalidaViewSet(viewsets.ModelViewSet):
    queryset = RegistroEntradaSalida.objects.all()
    serializer_class = RegistroEntradaSalidaSerializer
