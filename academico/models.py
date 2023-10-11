from django.db import models
from django.contrib.auth.models import User

class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    nombres = models.CharField(max_length=100)
    email = models.EmailField()
    especialidad = models.CharField(max_length=100)
    acceso_autorizado = models.BooleanField(default=False)
    activo = models.BooleanField(default=True)
    informacion_academica = models.TextField(blank=True, null=True)
    contrasenia = models.CharField(max_length=128)
    documento_identificacion = models.CharField(max_length=20)
    domicilio = models.TextField()
    email_laboral = models.EmailField()
    fecha_nacimiento = models.DateField()
    foto = models.ImageField(upload_to='docente_fotos/', blank=True, null=True)

class Periodo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion_corta = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombre_asignatura = models.CharField(max_length=100)
    area_de_estudio = models.CharField(max_length=100)
    aula = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    '''docente = models.ForeignKey(Docente, on_delete=models.CASCADE)'''
    curso = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_asignatura

class Horario(models.Model):
    profesor = models.ForeignKey(Docente, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)

    def __str__(self):
        return f'Horario de {self.asignatura} para {self.profesor} en {self.periodo}'

class HoraTemporada(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre if self.nombre else f'Hora Hábil para {self.periodo}'
