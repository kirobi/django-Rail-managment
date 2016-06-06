# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PythonLab', '0002_auto_20151212_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='cost',
            field=models.IntegerField(default=100, max_length=128),
        ),
        migrations.AlterField(
            model_name='train',
            name='name',
            field=models.CharField(default='Noname', max_length=128),
        ),
    ]
