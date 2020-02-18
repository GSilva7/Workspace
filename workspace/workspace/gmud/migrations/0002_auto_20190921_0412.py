# Generated by Django 2.2.5 on 2019-09-21 07:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('gmud', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gmud',
            name='hora',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Hora de Execução'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gmud',
            name='cliente',
            field=models.IntegerField(choices=[(1, 'Sage'), (2, 'Cetelem'), (3, 'Bradesco'), (4, 'Heineken'), (5, 'Guardian'), (6, 'Adtalem'), (7, 'Allergan')], verbose_name='Cliente'),
        ),
        migrations.AlterField(
            model_name='gmud',
            name='criticidade',
            field=models.IntegerField(choices=[(1, 'Nenhuma'), (2, 'Baixa'), (3, 'Media'), (4, 'Alta'), (5, 'Critico')], verbose_name='Criticidade'),
        ),
        migrations.AlterField(
            model_name='gmud',
            name='data',
            field=models.DateField(verbose_name='Data de Execução'),
        ),
        migrations.AlterField(
            model_name='gmud',
            name='procedimento',
            field=models.FileField(null=True, upload_to='procedimentos/', verbose_name='Procedimentos'),
        ),
        migrations.AlterField(
            model_name='gmud',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pendente'), (2, 'Aguardando Cliente'), (3, 'Aprovado'), (4, 'Reprovado'), (5, 'Finalizado')], default=1, verbose_name='Status'),
        ),
    ]
