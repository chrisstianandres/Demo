# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-04-10 19:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('silabo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='silabo',
            options={'ordering': ['-materia', '-semana', '-unidad', '-tema', '-clase'], 'verbose_name': 'silabo', 'verbose_name_plural': 'silabos'},
        ),
    ]
