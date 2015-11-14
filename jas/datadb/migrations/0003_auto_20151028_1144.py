# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0002_remove_hour_dt_observation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphdata',
            name='value_avg',
            field=models.DecimalField(verbose_name=b'   VALUE_AVG  ', max_digits=6, decimal_places=2),
        ),
    ]
