# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0015_agsstation_value_bc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agsstation',
            name='value_bc',
            field=models.DecimalField(max_digits=6, decimal_places=3),
        ),
    ]
