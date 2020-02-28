from django.db import models

# Create your models here.
class clientes(models.Model):
    nome = models.CharField(max_length=100, null=False)
    qtdpa = models.IntegerField()
    hrUra = models.TextField(null=True)
    servidores = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
    def __str__(self):
        return self.nome

