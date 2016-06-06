# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('PythonLab', '0001_initial')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('num', models.CharField(primary_key=True, unique=True, max_length=7, serialize=False)),
                ('cityFrom', models.CharField(default='Unknown', max_length=128)),
                ('cityTo', models.CharField(default='Unknown', max_length=128)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(null=True, max_length=128)),
                ('type', models.CharField(null=True, choices=[('rapid', 'High-speed'), ('season', 'Season'), ('local', 'Local'), ('disposable', 'One-way')], max_length=16)),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='trains',
            field=models.ManyToManyField(to='PythonLab.Train'),
        ),
    ]
