from django.contrib import admin

from .models import Docente, Periodo, Asignatura, Horario, HoraTemporada

admin.site.register(Docente)
admin.site.register(Periodo)
admin.site.register(Asignatura)
admin.site.register(Horario)
admin.site.register(HoraTemporada)