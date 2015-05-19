# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_projections_reservations'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projection',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('proj_type', models.CharField(max_length=120)),
                ('proj_date', models.DateField()),
                ('proj_time', models.CharField(max_length=60)),
                ('movie_id', models.ForeignKey(to='website.Movie')),
            ],
        ),
        migrations.RenameModel(
            old_name='Reservations',
            new_name='Reservation',
        ),
        migrations.RemoveField(
            model_name='projections',
            name='movie_id',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='projections',
            field=models.ManyToManyField(to='website.Projection'),
        ),
        migrations.DeleteModel(
            name='Projections',
        ),
    ]
