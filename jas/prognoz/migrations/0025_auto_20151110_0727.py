# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0024_settlements_bereg'),
    ]

    operations = [
        migrations.AddField(
            model_name='settlements',
            name='alarm_end',
            field=models.SmallIntegerField(default=1, verbose_name=b'\xd0\xa3\xd0\xb3\xd1\x80\xd0\xbe\xd0\xb7\xd0\xb0 \xd0\xb2\xd0\xba\xd0\xbe\xd0\xbd\xd1\x86\xd0\xb5'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settlements',
            name='alarm',
            field=models.SmallIntegerField(verbose_name=b'\xd0\xa3\xd0\xb3\xd1\x80\xd0\xbe\xd0\xb7\xd0\xb0 \xd0\xb2\xd0\xbd\xd0\xb0\xd1\x87\xd0\xb0\xd0\xbb\xd0\xb5'),
        ),
    ]
