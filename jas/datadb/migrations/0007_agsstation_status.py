# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0006_auto_20160104_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsstation',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
