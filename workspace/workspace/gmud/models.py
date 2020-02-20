from django.db import models


class gmud(models.Model):
    Clientes = [
        (1, 'Sage'),
        (2, 'Cetelem'),
        (3, 'Bradesco'),
        (4, 'Heineken'),
        (5, 'Guardian'),
        (6, 'Adtalem'),
        (7, 'Allergan'),
    ]
    Criticidades = [
        (1, 'Nenhuma'),
        (2, 'Baixa'),
        (3, 'Media'),
        (4, 'Alta'),
        (5, 'Critico')
    ]
    Status = [
        (1, 'Pendente'),
        (2, 'Aguardando Cliente'),
        (3, 'Aprovado'),
        (4, 'Reprovado'),
        (5, 'Finalizado'),
        (6, 'Rollback'),
    ]
    titulo = models.CharField('Titulo', max_length=100, null=False)
    cliente = models.IntegerField('Cliente', choices=Clientes)
    criticidade = models.IntegerField('Criticidade', choices=Criticidades)
    resumo = models.CharField('Resumo', max_length=400, blank=True)
    data = models.DateField('Data de Execução', null=False)
    hora = models.TimeField('Hora de Execução', null=False)
    datacriacao = models.DateTimeField('Data de Criação', auto_now=True)
    procedimento = models.FileField('Procedimentos', upload_to='procedimentos/', null=False)
    servidores = models.CharField('Servidores', max_length=100, blank=True)
    status = models.IntegerField('Status', choices=Status, default=1)
    resolucao = models.TextField('Resolucao', blank=True)

    def __str__(self):
        return self.titulo
    class Meta:
        verbose_name = 'GMUD'
        verbose_name_plural = "GMUDs"
