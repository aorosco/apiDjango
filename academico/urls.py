from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DocenteViewSet,
    PeriodoAcademicoViewSet,
    AsignaturaViewSet,
    HorarioViewSet,
    HoraTemporadaViewSet,
)

# Crea un enrutador
router = DefaultRouter()

# Registra las vistas de API en el enrutador
router.register(r'docentes', DocenteViewSet)
router.register(r'periodos-academicos', PeriodoAcademicoViewSet)
router.register(r'asignaturas', AsignaturaViewSet)
router.register(r'horarios', HorarioViewSet)
router.register(r'horas-temporada', HoraTemporadaViewSet)

# Define las rutas de la API
urlpatterns = [
    path('', include(router.urls)),
]

# Opcional: Puedes agregar rutas adicionales si es necesario
# urlpatterns += [
#     path('ruta-personalizada/', vista_personalizada),
# ]
