from django.db import models

class IPRESS(models.Model):
    cod = models.CharField(primary_key = True,max_length = 8, unique= True)
    nombre = models.CharField(max_length = 20)
    tipSeg =  models.CharField(max_length = 20)


# Create your models here.
