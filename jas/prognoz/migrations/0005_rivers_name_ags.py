# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0004_rivers_river_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='rivers',
            name='name_ags',
            field=models.TextField(default=1, max_length=60, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x81\xd1\x82\xd0\xb0\xd0\xbd\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=False,
        ),
    ]
