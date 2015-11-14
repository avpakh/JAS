# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0007_auto_20151031_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prognozdata',
            name='discharge',
            field=models.DecimalField(verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x85\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8', max_digits=12, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='prognozdata',
            name='distance',
            field=models.DecimalField(verbose_name=b' \xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe \xd1\x83\xd1\x81\xd1\x82\xd1\x8c\xd1\x8f ', max_digits=12, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='prognozdata',
            name='dno',
            field=models.DecimalField(verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb0 \xd0\xb4\xd0\xbd\xd0\xb0', max_digits=12, decimal_places=6),
        ),
        migrations.AlterField(
            model_name='prognozdata',
            name='level',
            field=models.DecimalField(verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8', max_digits=12, decimal_places=6),
        ),
    ]
