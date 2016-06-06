# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('num', models.CharField(primary_key=True, max_length=7, serialize=False, unique=True)),
                ('cityFrom', models.CharField(max_length=128, default='Unknown')),
                ('cityTo', models.CharField(max_length=128, default='Unknown')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128, null=True)),
                ('type', models.CharField(max_length=16, null=True, choices=[('rapid', 'High-speed'), ('season', 'Season'), ('local', 'Local'), ('disposable', 'One-way')])),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='trains',
            field=models.ManyToManyField(to='PythonLab.Train'),
        ),
    ]
