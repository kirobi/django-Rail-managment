# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PythonLab', '0004_auto_20151212_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='train',
            name='name',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='cost',
            field=models.IntegerField(default=100),
        ),
    ]
