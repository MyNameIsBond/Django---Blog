# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-28 00:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='pub_date',
            field=models.DateField(null=True),
        ),
    ]
