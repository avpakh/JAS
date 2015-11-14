# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0012_auto_20151101_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapsbrovka',
            name='brovka0_40',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9e\xd1\x82 0  \xd0\xb4\xd0\xbe 40 \xd1\x81\xd0\xbc \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9 ', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='mapsbrovka',
            name='brovka40_1',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9e\xd1\x82 40 \xd1\x81\xd0\xbc \xd0\xb4\xd0\xbe 1 \xd0\xbc \xd0\xbf\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9', max_digits=5, decimal_places=2, blank=True),
        ),
    ]
