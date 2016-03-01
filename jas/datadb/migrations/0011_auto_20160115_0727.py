# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0010_graphdatabc'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsstation',
            name='status_level',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='agsstation',
            name='value_zero',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
