# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mapflood',
            name='image',
        ),
        migrations.AddField(
            model_name='mapflood',
            name='mapflood_image',
            field=sorl.thumbnail.fields.ImageField(default=1, upload_to=b'maps/static/im/'),
            preserve_default=False,
        ),
    ]
