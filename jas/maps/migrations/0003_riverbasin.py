# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_auto_20151102_0615'),
    ]

    operations = [
        migrations.CreateModel(
            name='RiverBasin',
            fields=[
                ('id_riverbasin', models.AutoField(serialize=False, primary_key=True)),
                ('river_basin', models.TextField(max_length=120, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb1\xd0\xb0\xd1\x81\xd1\x81\xd0\xb5\xd0\xb9\xd0\xbd\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8')),
            ],
            options={
                'db_table': 'RiverBasin',
                'managed': True,
            },
        ),
    ]
