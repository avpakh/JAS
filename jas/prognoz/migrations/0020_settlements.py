# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djgeojson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0019_site_new_xaxis'),
    ]

    operations = [
        migrations.CreateModel(
            name='Settlements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd1\x81\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe \xd0\xbf\xd1\x83\xd0\xbd\xd0\xba\xd1\x82\xd0\xb0')),
                ('geom', djgeojson.fields.PolygonField()),
            ],
        ),
    ]
