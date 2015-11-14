# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0022_auto_20151109_1351'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlements',
            name='end',
            field=models.DecimalField(default=1, verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbf\xd0\xbe \xd1\x80\xd0\xb5\xd0\xba\xd0\xb5 \xd0\xaf\xd1\x81\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xb4\xd0\xb0 - \xd0\xba\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x86, \xd0\xba\xd0\xbc', max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settlements',
            name='end_alarm',
            field=models.DecimalField(default=1, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb0 \xd0\xbe\xd0\xbf\xd0\xb0\xd1\x81\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8 - \xd0\xba\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x86, \xd0\xbc \xd0\x91\xd0\xa1', max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settlements',
            name='end_brovka',
            field=models.DecimalField(default=1, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb0 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8 \xd0\xaf\xd1\x81\xd0\xb5\xd0\xbb\xd1\x8c\xd0\xb4\xd1\x8b - \xd0\xba\xd0\xbe\xd0\xbd\xd0\xb5\xd1\x86, \xd0\xbc \xd0\x91\xd0\xa1', max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
