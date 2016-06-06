# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PythonLab', '0005_auto_20151212_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='name',
            field=models.CharField(max_length=128, default='Unknown'),
        ),
    ]
