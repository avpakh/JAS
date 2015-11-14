# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0004_auto_20151028_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphdata',
            name='dt_observation',
            field=models.DateTimeField(verbose_name=b'\xd0\xa7\xd0\xb0\xd1\x81/\xd0\x94\xd0\xb5\xd0\xbd\xd1\x8c'),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='value_avg',
            field=models.DecimalField(verbose_name=b'   \xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xbe\xd1\x82 \xd0\xbe\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb8 0 \xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd1\x86\xd0\xb8\xd0\xb8 \xd0\x90\xd0\x93\xd0\xa1 ', max_digits=6, decimal_places=2),
        ),
    ]
