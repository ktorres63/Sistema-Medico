from django.db import models
from Medico.models import Medico

class Paciente(models.Model):
    dni = models.CharField(primary_key = True,max_length = 8, unique=True)
    nombre = models.CharField(max_length = 20)
    apPat= models.CharField(max_length = 20)
    apMat= models.CharField(max_length = 20)
    telf = models.CharField(max_length = 6)
    edad = models.IntegerField()
    dir = models.CharField(max_length = 30)
    fechNac = models.DateField()
    medico = models.ForeignKey(Medico, null = True, blank = True, on_delete = models.CASCADE)

    def __str__(self):
        return "{} {}. {}".format(self.apPat,self.apMat,self.nombre)
