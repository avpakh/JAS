# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0011_auto_20160115_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsstation',
            name='datetime_text',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
