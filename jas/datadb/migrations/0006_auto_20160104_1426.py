# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0005_auto_20151102_0556'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsstation',
            name='station_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agsstation',
            name='value_level',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
