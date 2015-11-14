# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0016_auto_20151101_2204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapsdata',
            name='river',
            field=models.ForeignKey(to='prognoz.Rivers', blank=True),
        ),
    ]
