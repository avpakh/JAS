# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0018_site_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_new',
            name='xaxis',
            field=models.SmallIntegerField(default=0, verbose_name=b'z'),
            preserve_default=False,
        ),
    ]
