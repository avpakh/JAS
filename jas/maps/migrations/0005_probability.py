# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_typemap'),
    ]

    operations = [
        migrations.CreateModel(
            name='Probability',
            fields=[
                ('id_probability', models.AutoField(serialize=False, primary_key=True)),
                ('name_probability', models.TextField(max_length=100, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd0\xbe\xd0\xb1\xd0\xb5\xd1\x81\xd0\xbf\xd0\xb5\xd1\x87\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd1\x81\xd1\x82\xd0\xb8')),
            ],
        ),
    ]
