# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ids', models.SmallIntegerField(verbose_name=b'IDS')),
                ('dt', models.DateTimeField(verbose_name=b'DT')),
                ('mid', models.SmallIntegerField(verbose_name=b'MID')),
                ('data', models.FloatField(verbose_name=b'DATA')),
            ],
            options={
                'db_table': '_DATA',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AgsStation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('geom', djgeojson.fields.PointField()),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to=b'')),
            ],
            options={
                'db_table': 'Agstation',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Av',
            fields=[
                ('id_table', models.AutoField(serialize=False, primary_key=True)),
                ('id_station', models.SmallIntegerField(verbose_name=b'ID_STATION')),
                ('date_observation', models.DateField(verbose_name=b'  DATA_OBS  ')),
                ('value_min', models.DecimalField(verbose_name=b'   VALUE_MIN   ', max_digits=6, decimal_places=2)),
                ('value_max', models.DecimalField(verbose_name=b'   VALUE_MAX   ', max_digits=6, decimal_places=2)),
                ('value_avg', models.DecimalField(verbose_name=b'   VALUE_AV   ', max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'Av',
            },
        ),
        migrations.CreateModel(
            name='DataAnalys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_analys', models.SmallIntegerField(verbose_name=b'ID_ANALYS')),
                ('analys_type', models.TextField(verbose_name=b'TYPE')),
            ],
            options={
                'db_table': 'DataAnalys',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='GraphData',
            fields=[
                ('id_table', models.AutoField(serialize=False, primary_key=True)),
                ('id_station', models.SmallIntegerField(verbose_name=b'ID_STATION')),
                ('dt_observation', models.DateTimeField(verbose_name=b'DT_OBS')),
                ('date_observation', models.DateField(verbose_name=b'DATA_OBS')),
                ('hour', models.SmallIntegerField(verbose_name=b'HOUR')),
                ('value_min', models.DecimalField(verbose_name=b'   VALUE_MIN   ', max_digits=6, decimal_places=2)),
                ('value_max', models.DecimalField(verbose_name=b'   VALUE_MAX   ', max_digits=6, decimal_places=2)),
                ('value_avg', models.DecimalField(verbose_name=b'   VALUE_AV   ', max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'GraphData',
            },
        ),
        migrations.CreateModel(
            name='Hour',
            fields=[
                ('id_table', models.AutoField(serialize=False, primary_key=True)),
                ('id_station', models.SmallIntegerField(verbose_name=b'ID_STATION')),
                ('dt_observation', models.DateTimeField(verbose_name=b'DT_OBS')),
                ('date_observation', models.DateField(verbose_name=b'DATA_OBS')),
                ('hour', models.SmallIntegerField(verbose_name=b'HOUR')),
                ('value_min', models.DecimalField(verbose_name=b'   VALUE_MIN   ', max_digits=6, decimal_places=2)),
                ('value_max', models.DecimalField(verbose_name=b'   VALUE_MAX   ', max_digits=6, decimal_places=2)),
                ('value_avg', models.DecimalField(verbose_name=b'   VALUE_AV   ', max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'Hour',
            },
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_station', models.SmallIntegerField(verbose_name=b'ID_STATION')),
                ('description', models.TextField(verbose_name=b'Description')),
            ],
            options={
                'db_table': 'Station',
                'managed': True,
            },
        ),
    ]
