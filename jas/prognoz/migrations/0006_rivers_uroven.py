# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0005_rivers_name_ags'),
    ]

    operations = [
        migrations.AddField(
            model_name='rivers',
            name='uroven',
            field=models.DecimalField(default=1, verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb0 \xd0\x91\xd0\xa1', max_digits=6, decimal_places=2),
            preserve_default=False,
        ),
    ]
