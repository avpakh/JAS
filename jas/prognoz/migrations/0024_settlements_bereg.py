# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0023_auto_20151109_1354'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlements',
            name='bereg',
            field=models.CharField(default=1, max_length=20, verbose_name=b'\xd0\x91\xd0\xb5\xd1\x80\xd0\xb5\xd0\xb3'),
            preserve_default=False,
        ),
    ]
