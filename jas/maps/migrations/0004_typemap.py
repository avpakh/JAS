# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0003_riverbasin'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeMap',
            fields=[
                ('id_typemap', models.AutoField(serialize=False, primary_key=True)),
                ('typemap', models.TextField(max_length=120, verbose_name=b'\xd0\x92\xd0\xb8\xd0\xb4 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b')),
            ],
            options={
                'db_table': 'TypeMap',
                'managed': True,
            },
        ),
    ]
