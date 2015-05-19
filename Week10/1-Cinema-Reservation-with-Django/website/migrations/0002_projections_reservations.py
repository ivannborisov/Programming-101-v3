# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projections',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('proj_type', models.CharField(max_length=120)),
                ('proj_date', models.DateField()),
                ('proj_time', models.CharField(max_length=60)),
                ('movie_id', models.ForeignKey(to='website.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('username', models.CharField(max_length=30)),
                ('row', models.PositiveSmallIntegerField()),
                ('col', models.PositiveSmallIntegerField()),
                ('projections', models.ManyToManyField(to='website.Projections')),
            ],
        ),
    ]
