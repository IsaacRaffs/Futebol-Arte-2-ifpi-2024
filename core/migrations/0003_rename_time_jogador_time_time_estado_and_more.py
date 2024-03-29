# Generated by Django 5.0 on 2024-02-29 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cep', '0001_initial'),
        ('core', '0002_time_foto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jogador',
            old_name='Time',
            new_name='time',
        ),
        migrations.AddField(
            model_name='time',
            name='estado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cep.estado'),
        ),
        migrations.AlterField(
            model_name='titulos',
            name='time',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.time'),
        ),
    ]
