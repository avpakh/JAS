# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0008_agsstation_explanation'),
    ]

    operations = [
        migrations.AddField(
            model_name='agsstation',
            name='description_ru',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
