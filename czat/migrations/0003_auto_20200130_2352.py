# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2020-01-30 22:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('czat', '0002_auto_20200128_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nieobecnosc',
            name='data_koniec',
            field=models.DateField(verbose_name='data ostatniego dnia nieobecnosci'),
        ),
        migrations.AlterField(
            model_name='nieobecnosc',
            name='data_start',
            field=models.DateField(verbose_name='data pierwszego dnia nieobecnosci'),
        ),
    ]
