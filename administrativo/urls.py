from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistroEntradaSalidaViewSet

router = DefaultRouter()
router.register(r'registros', RegistroEntradaSalidaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
