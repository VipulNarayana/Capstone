# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-24 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0008_auto_20160424_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='flag',
            field=models.IntegerField(null=True),
        ),
    ]
