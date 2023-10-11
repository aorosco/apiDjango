from rest_framework import serializers
from .models import RegistroEntradaSalida

class RegistroEntradaSalidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroEntradaSalida
        fields = '__all__'
