# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0012_mapimage_mapdescr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapimage',
            name='map_image',
            field=sorl.thumbnail.fields.ImageField(upload_to=b'/static/im/', blank=True),
        ),
    ]
