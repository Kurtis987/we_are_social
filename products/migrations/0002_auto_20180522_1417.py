# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-05-22 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=254),
        ),
    ]
