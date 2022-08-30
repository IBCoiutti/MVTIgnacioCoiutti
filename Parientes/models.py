from django.db import models

# Create your models here.



class Pariente(models.model):
    Nombre=models.CharField(max_length=50)
    Edad=models.IntegerField()
    Fecha_Nac=models.DateField()
    Parentesco=models.CharField(max_length=50)
