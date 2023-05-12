from django.db import models
from django.utils import timezone

class Program(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    update_date = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name
    
class Teacher(models.Model):

    class Position(models.TextChoices):
        TRAINER = 'F', 'Formador'
        COTRAINER = 'CF', 'Coformador'

    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    position = models.CharField(max_length=2,choices=Position.choices, default=Position.TRAINER)

    def __str__(self):
        return self.name

class Cohorte(models.Model):
    name = models.CharField(max_length=250)
    start_date = models.DateField
    end_date = models.DateField
    duration = models.IntegerField
    number_hours = models.IntegerField
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    kind = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class TeacherCohorte(models.Model):
    id_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    id_cohorte = models.ForeignKey(Cohorte, on_delete=models.CASCADE)
