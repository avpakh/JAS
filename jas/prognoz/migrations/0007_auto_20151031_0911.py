# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0006_rivers_uroven'),
    ]

    operations = [
        migrations.CreateModel(
            name='FloodClassification',
            fields=[
                ('id_class', models.AutoField(serialize=False, primary_key=True)),
                ('map_index', models.SmallIntegerField(verbose_name=b'\xd0\x9a\xd0\xbe\xd0\xb4 \xd0\xba\xd0\xb0\xd1\x80\xd1\x82\xd1\x8b')),
                ('description', models.TextField(max_length=120, verbose_name=b'\xd0\x9a\xd0\xbb\xd0\xb0\xd1\x81\xd1\x81\xd0\xb8\xd1\x84\xd0\xb8\xd0\xba\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbd\xd0\xb0\xd0\xb2\xd0\xbe\xd0\xb4\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb9')),
            ],
            options={
                'db_table': 'FloodClassification',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='rivers',
            name='data_avaliable',
            field=models.BooleanField(default=1, verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xbb\xd0\xb8\xd1\x87\xd0\xb8\xd0\xb5 \xd0\xbe\xd0\xbf\xd0\xb5\xd1\x80\xd0\xb0\xd1\x82\xd0\xb8\xd0\xb2\xd0\xbd\xd0\xbe\xd0\xb9 \xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'),
            preserve_default=False,
        ),
    ]
