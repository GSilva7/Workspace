from django.db import models

# Create your models here.
class clientes(models.Model):
    nome = models.CharField(max_length=100, null=False)
    qtdpa = models.IntegerField()

