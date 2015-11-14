# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0009_prognozdata_distance_float'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapsBrovka',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance_float', models.FloatField(verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe \xd1\x83\xd1\x81\xd1\x82\xd1\x8c\xd1\x8f \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8')),
                ('brovka_below', models.DecimalField(verbose_name=b'\xd0\x9d\xd0\xb8\xd0\xb6\xd0\xb5 0', max_digits=5, decimal_places=2)),
                ('brovka0_40', models.DecimalField(verbose_name=b'\xd0\x9e\xd1\x82 0 - 40', max_digits=5, decimal_places=2)),
                ('brovka40_1', models.DecimalField(verbose_name=b'\xd0\x9e\xd1\x82 40 - 1', max_digits=5, decimal_places=2)),
                ('brovka1_3', models.DecimalField(verbose_name=b'\xd0\x9e\xd1\x82 1 - 30', max_digits=5, decimal_places=2)),
            ],
            options={
                'db_table': 'MapsBrovka',
                'managed': True,
            },
        ),
    ]
