from pickle import TRUE
from django.db import models


class Usuario(models.Model):

    def __str__(self) :
        return f"{self.nombre}"

    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    documento= models.IntegerField()
    email= models.EmailField(max_length=254, null= TRUE )
    pais= models.CharField(max_length=60)
    provincia= models.CharField(max_length=30)
    

class Juego(models.Model):

    def __str__(self) :
        return f"{self.titulo}"

    titulo= models.CharField(max_length=30)
    descripcion= models.CharField(max_length=70)
    genero= models.CharField(max_length=30)
    fecha_de_estreno= models.DateField()
    tipo_de_juego= models.CharField(max_length=60)
    caratula= models.ImageField(upload_to = 'juegos', null=TRUE, blank=TRUE)
