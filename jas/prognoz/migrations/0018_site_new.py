# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0017_auto_20151101_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site_New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.FloatField(verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe \xd1\x83\xd1\x81\xd1\x82\xd1\x8c\xd1\x8f')),
                ('explanation', models.TextField(verbose_name=b'\xd0\x9e\xd0\xb1\xd1\x8a\xd0\xb5\xd0\xba\xd1\x82')),
                ('river', models.ForeignKey(to='prognoz.Rivers')),
            ],
            options={
                'db_table': 'Site_New',
                'managed': True,
            },
        ),
    ]
