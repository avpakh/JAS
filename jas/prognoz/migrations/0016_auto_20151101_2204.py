# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0015_mapsdata_river'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapsdata',
            name='distance_float',
            field=models.FloatField(null=True, verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe \xd1\x83\xd1\x81\xd1\x82\xd1\x8c\xd1\x8f \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8', blank=True),
        ),
    ]
