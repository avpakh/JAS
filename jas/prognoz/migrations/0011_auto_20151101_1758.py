# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0010_mapsbrovka'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapsbrovka',
            name='brovka0_40',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9e\xd1\x82 0 - 40', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='mapsbrovka',
            name='brovka1_3',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9e\xd1\x82 1 - 30', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='mapsbrovka',
            name='brovka40_1',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9e\xd1\x82 40 - 1', max_digits=5, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='mapsbrovka',
            name='brovka_below',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\x9d\xd0\xb8\xd0\xb6\xd0\xb5 0', max_digits=5, decimal_places=2, blank=True),
        ),
    ]
