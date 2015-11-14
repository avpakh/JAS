# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0014_mapsdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapsdata',
            name='river',
            field=models.ForeignKey(default=1, to='prognoz.Rivers'),
            preserve_default=False,
        ),
    ]
