# Generated by Django 2.0.6 on 2020-03-05 21:46

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('alumno', '0001_initial'),
        ('curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ciclo', models.IntegerField(choices=[(1, 'Primero'), (2, 'Segundo')], default=1)),
                ('año', models.DateField(default=datetime.datetime.now)),
                ('alumno', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='alumno.Alumno')),
                ('curso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='curso.Curso')),
            ],
        ),
    ]
