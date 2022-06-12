from django.db import models


# Create your models here.

class Tipo_Usuario(models.Model):
    tipo = models.CharField(max_length=15)

    def __str__(self):
        return self.cargo


class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nom_usuario = models.CharField(max_length=15)
    contrasena = models.CharField(max_length=15)
    tipo = models.ForeignKey(Tipo_Usuario, on_delete=models.CASCADE)


class Mesas(models.Model):
    nSerie = models.CharField(max_length=50)


class Tipo_Comida(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Platillos(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    precio = models.FloatField()
    tipo = models.ForeignKey(Tipo_Comida, on_delete=models.CASCADE)


class Tipo_Bebida(models.Model):
    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Bebidas(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    tipo = models.ForeignKey(Tipo_Bebida, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Tipo_Ingrediente(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Ingredientes(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.ForeignKey(Tipo_Ingrediente, on_delete=models.CASCADE)
