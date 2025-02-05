# Generated by Django 2.2.5 on 2019-09-21 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmud', '0003_auto_20190921_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gmud',
            name='procedimento',
            field=models.FileField(upload_to='procedimentos/', verbose_name='Procedimentos'),
        ),
        migrations.AlterField(
            model_name='gmud',
            name='status',
            field=models.IntegerField(choices=[(1, 'Pendente'), (2, 'Aguardando Cliente'), (3, 'Aprovado'), (4, 'Reprovado'), (5, 'Finalizado')], default=1, verbose_name='Status'),
        ),
    ]
