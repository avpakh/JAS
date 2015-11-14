# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0017_auto_20151101_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapFlood',
            fields=[
                ('id_class', models.AutoField(serialize=False, primary_key=True)),
                ('map_index', models.SmallIntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b')),
                ('description', models.TextField(max_length=120, verbose_name=b'O\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b')),
                ('image', models.ImageField(upload_to=b'maps/static/im/')),
                ('river', models.ForeignKey(to='prognoz.Rivers')),
            ],
            options={
                'db_table': 'MapFlood',
                'managed': True,
            },
        ),
    ]
