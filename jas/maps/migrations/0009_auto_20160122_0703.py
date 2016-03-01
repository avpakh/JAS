# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0008_auto_20160122_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapimage',
            name='map_image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'maps/static/im/', blank=True),
        ),
    ]
