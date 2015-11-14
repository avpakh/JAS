# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0025_auto_20151110_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlements',
            name='description',
            field=models.CharField(default=1, max_length=60, verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb8\xd1\x81\xd0\xba\xd0\xb0'),
            preserve_default=False,
        ),
    ]
