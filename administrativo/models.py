from django.db import models

class RegistroEntradaSalida(models.Model):
    emp_no = models.IntegerField()  # Número de Empleado
    ac_no = models.IntegerField()  # Número de Control de Acceso
    numero = models.IntegerField()  # Número
    name = models.CharField(max_length=100)  # Nombre
    auto_assign = models.BooleanField()  # Asignación Automática
    date = models.DateField()  # Fecha
    timetable = models.TimeField()  # Horario
    on_duty = models.TimeField()  # En Servicio
    off_duty = models.TimeField()  # Fuera de Servicio
    clock_in = models.TimeField()  # Registro de Entrada
    clock_out = models.TimeField()  # Registro de Salida

    def __str__(self):
        return f"Registro {self.numero} de {self.name}"
