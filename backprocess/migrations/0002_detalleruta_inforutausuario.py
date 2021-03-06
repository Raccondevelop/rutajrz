# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 17:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backprocess', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleRuta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_espera', models.IntegerField(default=0)),
                ('t_total', models.IntegerField(default=0)),
                ('detalle', models.TextField(null=True)),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backprocess.Ruta')),
            ],
        ),
        migrations.CreateModel(
            name='InfoRutaUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_espera', models.IntegerField(default=0)),
                ('t_total', models.IntegerField(default=0)),
                ('rating', models.IntegerField(default=5)),
                ('ruta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backprocess.Ruta')),
            ],
        ),
    ]
