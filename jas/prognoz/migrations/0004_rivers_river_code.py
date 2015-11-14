# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0003_maps_map_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='rivers',
            name='river_code',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xd0\xa3\xd0\xbd\xd0\xb8\xd0\xba\xd0\xb0\xd0\xbb\xd1\x8c\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xba\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8'),
            preserve_default=False,
        ),
    ]
