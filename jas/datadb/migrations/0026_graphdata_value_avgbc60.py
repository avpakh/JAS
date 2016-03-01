# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0025_auto_20160211_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='graphdata',
            name='value_avgBC60',
            field=models.DecimalField(null=True, verbose_name=b'1', max_digits=6, decimal_places=3),
        ),
    ]
