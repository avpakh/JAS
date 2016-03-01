# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0010_mapimage_part_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapimage',
            name='mapcode',
            field=models.TextField(max_length=10, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b', blank=True),
        ),
    ]
