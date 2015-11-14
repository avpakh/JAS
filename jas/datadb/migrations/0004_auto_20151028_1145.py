# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0003_auto_20151028_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphdata',
            name='value_avg',
            field=models.DecimalField(verbose_name=b'   \xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0  ', max_digits=6, decimal_places=2),
        ),
    ]
