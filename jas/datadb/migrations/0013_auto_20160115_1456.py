# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0012_agsstation_datetime_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agsstation',
            name='value_level',
            field=models.DecimalField(max_digits=6, decimal_places=2),
        ),
    ]
