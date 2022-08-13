from django.db import models

class Medico(models.Model):
    dni = models.CharField(primary_key = True,max_length = 8, unique=True)
    nombre = models.CharField(max_length = 20)
    apPat= models.CharField(max_length = 20)
    apMat = models.CharField(max_length = 20)
    nColMed = models.CharField(max_length = 20)
    def __str__(self):
        return "{}-{},{}".format(self.dni,self.apPat, self.nombre)
    

class Jefe(models.Model):
    dni = models.CharField(primary_key = True,max_length = 8)
    nombre = models.CharField(max_length = 20)
    apPat= models.CharField(max_length = 20)
    apMat = models.CharField(max_length = 20)
    titulo = models.CharField(max_length = 25)
