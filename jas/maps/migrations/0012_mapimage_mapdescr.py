# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0011_auto_20160129_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapimage',
            name='mapdescr',
            field=models.TextField(max_length=100, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b', blank=True),
        ),
    ]
