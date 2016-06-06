# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PythonLab', '0003_auto_20151212_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='cost',
            field=models.IntegerField(default=100),
        ),
    ]
