# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0013_auto_20160115_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsstation',
            name='value_brovka',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
