# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 14:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0004_auto_20160423_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=10)),
                ('flag', models.CharField(max_length=5)),
                ('time', models.TimeField()),
            ],
        ),
    ]
