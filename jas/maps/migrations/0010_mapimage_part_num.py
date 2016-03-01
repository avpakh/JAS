# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0009_auto_20160122_0703'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapimage',
            name='part_num',
            field=models.IntegerField(default=1, blank=True),
            preserve_default=False,
        ),
    ]
