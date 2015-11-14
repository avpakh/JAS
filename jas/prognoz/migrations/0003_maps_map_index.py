# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0002_rivers_riverfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='maps',
            name='map_index',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b'),
            preserve_default=False,
        ),
    ]
