# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Maps',
            fields=[
                ('id_maps', models.AutoField(serialize=False, primary_key=True)),
                ('map_level', models.DecimalField(verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x87\xd0\xb5\xd1\x82\xd0\xbd\xd1\x8b\xd0\xb9 \xd1\x83\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c', max_digits=6, decimal_places=2)),
            ],
            options={
                'db_table': 'Maps',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Prognozdata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('distance', models.DecimalField(verbose_name=b' \xd0\xa0\xd0\xb0\xd1\x81\xd1\x81\xd1\x82\xd0\xbe\xd1\x8f\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb4\xd0\xbe \xd1\x83\xd1\x81\xd1\x82\xd1\x8c\xd1\x8f ', max_digits=6, decimal_places=2)),
                ('discharge', models.DecimalField(verbose_name=b'\xd0\xa0\xd0\xb0\xd1\x81\xd1\x85\xd0\xbe\xd0\xb4 \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8', max_digits=6, decimal_places=2)),
                ('level', models.DecimalField(verbose_name=b'\xd0\xa3\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8', max_digits=6, decimal_places=2)),
                ('dno', models.DecimalField(verbose_name=b'\xd0\x9e\xd1\x82\xd0\xbc\xd0\xb5\xd1\x82\xd0\xba\xd0\xb0 \xd0\xb4\xd0\xbd\xd0\xb0', max_digits=6, decimal_places=2)),
                ('time60', models.DecimalField(verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb2 \xd1\x87\xd0\xb0\xd1\x81\xd0\xb0\xd1\x85:\xd0\xbc\xd0\xb8\xd0\xbd\xd1\x83\xd1\x82\xd0\xb0\xd1\x85', max_digits=5, decimal_places=2)),
                ('time100', models.DecimalField(verbose_name=b'\xd0\x92\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb2 \xd1\x87\xd0\xb0\xd1\x81\xd0\xb0\xd1\x85', max_digits=5, decimal_places=2)),
                ('brovka', models.DecimalField(verbose_name=b'\xd0\x9f\xd1\x80\xd0\xb5\xd0\xb2\xd1\x8b\xd1\x88\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xbd\xd0\xb0\xd0\xb4 \xd0\xb1\xd1\x80\xd0\xbe\xd0\xb2\xd0\xba\xd0\xbe\xd0\xb9', max_digits=5, decimal_places=2)),
                ('map', models.ForeignKey(to='prognoz.Maps')),
            ],
            options={
                'db_table': 'PrognozData',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Rivers',
            fields=[
                ('id_river', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.TextField(verbose_name=b'\xd0\x9d\xd0\xb0\xd0\xb7\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8')),
            ],
            options={
                'db_table': 'Rivers',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='prognozdata',
            name='river',
            field=models.ForeignKey(to='prognoz.Rivers'),
        ),
        migrations.AddField(
            model_name='maps',
            name='river',
            field=models.ForeignKey(to='prognoz.Rivers'),
        ),
    ]
