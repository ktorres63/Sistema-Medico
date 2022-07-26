from django.db import models

class Medico(models.Model):
    dni = models.CharField(primary_key = True,max_length = 8)
    nombre = models.CharField(max_length = 20)
    apPat= models.CharField(max_length = 20)
    apMat = models.CharField(max_length = 20)
    nColMed = models.CharField(max_length = 20)

class Paciente(models.Model):
    dni = models.CharField(primary_key = True,max_length = 8)
    nombre = models.CharField(max_length = 20)
    apPat= models.CharField(max_length = 20)
    telf = models.CharField(max_length = 6)
    edad = models.IntegerField()
    dir = models.CharField(max_length = 6)
    fechNac = models.DateField()

class Jefe(models.Model):
    dni = models.CharField(primary_key = True,max_length = 8)
    nombre = models.CharField(max_length = 20)
    apPat= models.CharField(max_length = 20)
    apMat = models.CharField(max_length = 20)
    titulo = models.CharField(max_length = 25)

class IPRESS(models.Model):
    cod = models.CharField(primary_key = True,max_length = 8)
    nombre = models.CharField(max_length = 20)
    tipSeg =  models.CharField(max_length = 20)
