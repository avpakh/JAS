# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0020_settlements'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlements',
            name='alarm',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xd0\xa3\xd0\xb3\xd1\x80\xd0\xbe\xd0\xb7\xd0\xb0'),
            preserve_default=False,
        ),
    ]
