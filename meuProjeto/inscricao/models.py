from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=120)
    telefone = models.CharField(max_length=20)
    idade = models.IntegerField()
