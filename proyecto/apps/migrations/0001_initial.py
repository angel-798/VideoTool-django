# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-03 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('contrasena', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('resumen', models.TextField(null=True)),
                ('archivo', models.FileField(upload_to='media/')),
                ('numeroVisto', models.IntegerField(default='0')),
                ('numeroBuscado', models.IntegerField(default='0')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.Usuario')),
            ],
        ),
    ]
