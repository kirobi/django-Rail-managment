# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PythonLab', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('cost', models.CharField(null=True, max_length=128)),
                ('paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='route',
            name='trains',
        ),
        migrations.RemoveField(
            model_name='train',
            name='type',
        ),
        migrations.AddField(
            model_name='train',
            name='cityFrom',
            field=models.CharField(default='Unknown', max_length=128),
        ),
        migrations.AddField(
            model_name='train',
            name='cityTo',
            field=models.CharField(default='Unknown', max_length=128),
        ),
        migrations.AddField(
            model_name='train',
            name='cost',
            field=models.CharField(null=True, max_length=128),
        ),
        migrations.AddField(
            model_name='train',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.DeleteModel(
            name='Route',
        ),
        migrations.AddField(
            model_name='invoice',
            name='train',
            field=models.ForeignKey(to='PythonLab.Train'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
