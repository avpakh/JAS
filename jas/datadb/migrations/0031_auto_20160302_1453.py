# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0030_auto_20160302_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestav',
            name='value_avgBC50',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c - 50 \xd1\x81\xd0\xbc \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9', max_digits=6, decimal_places=3),
        ),
        migrations.AddField(
            model_name='requestav',
            name='value_avgBC60',
            field=models.DecimalField(null=True, verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xb4\xd0\xbe \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xb8', max_digits=6, decimal_places=3),
        ),
    ]
