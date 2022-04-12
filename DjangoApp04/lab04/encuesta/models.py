from django.db import models

# Create your models here.
class region(models.Model):
    nombre=models.CharField(max_length=200)

class Candidato(models.Model):
    nombre = models.CharField(max_length=200)
    partido = models.CharField(max_length=200)
    id_region = models.ForeignKey(region, in_delete=models.CASCADE)
    votos = models.IntegerField(default=0)
