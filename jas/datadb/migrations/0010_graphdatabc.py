# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0009_agsstation_description_ru'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphDataBC',
            fields=[
                ('id_table', models.AutoField(serialize=False, primary_key=True)),
                ('id_station', models.SmallIntegerField(verbose_name=b'ID_STATION')),
                ('dt_observation', models.DateTimeField(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81/\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c')),
                ('date_observation', models.DateField(verbose_name=b'DATA_OBS')),
                ('hour', models.SmallIntegerField(verbose_name=b'HOUR')),
                ('value_min', models.DecimalField(verbose_name=b'   VALUE_MIN   ', max_digits=6, decimal_places=2)),
                ('value_max', models.DecimalField(verbose_name=b'   VALUE_MAX   ', max_digits=6, decimal_places=2)),
                ('value_avg', models.DecimalField(verbose_name=b'   \xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xb2\xd0\xbe\xd0\xb4\xd1\x8b \xd0\xb2 \xd0\xb0\xd0\xb1\xd1\x81\xd0\xbe\xd0\xbb\xd1\x8e\xd1\x82\xd0\xbd\xd1\x8b\xd1\x85 \xd0\xbe\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb0\xd1\x85 \xd0\x91\xd0\xb0\xd0\xbb\xd1\x82\xd0\xb8\xd0\xb9\xd1\x81\xd0\xba\xd0\xbe\xd0\xb9 \xd1\x81\xd0\xb8\xd1\x81\xd1\x82\xd0\xb5\xd0\xbc\xd1\x8b(\xd0\x91\xd0\xa1)', max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'GraphDataBC',
            },
        ),
    ]
