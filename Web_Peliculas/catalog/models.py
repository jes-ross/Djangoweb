from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=64, help_text="Pon el nombre del genero")

    def __str__(self):
        return self.name

class Director(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre del director")

    def __str__(self):
        return self.name

class Film(models.Model):
    name = models.CharField(max_length=64, help_text="Nombre de la pelicula")

    def __str__(self):
        return self.name