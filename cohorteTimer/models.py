from django.db import models
from django.utils import timezone

class Programa(models.Model):
    nombre = models.CharField(max_length=250)
    descripcion = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    actualizado = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nombre
    
class Profesor(models.Model):

    class Cargo(models.TextChoices):
        FORMADOR = 'F', 'Formador'
        COFORMADOR = 'CF', 'Coformador'

    nombre = models.CharField(max_length=250)
    apellido = models.CharField(max_length=250)
    cargo = models.CharField(max_length=2,choices=Cargo.choices, default=Cargo.FORMADOR)

class Cohorte(models.Model):
    nombre = models.CharField(max_length=250)
    fecha_inicio = models.DateField
    fecha_finalizacion = models.DateField
    duracion = models.IntegerField
    cantidad_horas = models.IntegerField
    programa = models.ForeignKey(Programa, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=250)

class ProfesorCohorte(models.Model):
    id_profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    id_cohorte = models.ForeignKey(Cohorte, on_delete=models.CASCADE)
