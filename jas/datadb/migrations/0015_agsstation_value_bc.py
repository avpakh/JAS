# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0014_agsstation_value_brovka'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsstation',
            name='value_bc',
            field=models.DecimalField(default=1, max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
