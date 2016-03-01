# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datadb', '0022_auto_20160211_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphdata',
            name='value_avgBC',
            field=models.DecimalField(null=True, verbose_name=b'1', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='value_avgBC1',
            field=models.DecimalField(null=True, verbose_name=b'1', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='value_avgBC2',
            field=models.DecimalField(null=True, verbose_name=b'2', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='value_avgBC3',
            field=models.DecimalField(null=True, verbose_name=b'3', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='value_avgBC4',
            field=models.DecimalField(null=True, verbose_name=b'4', max_digits=6, decimal_places=3),
        ),
        migrations.AlterField(
            model_name='graphdata',
            name='value_avgBC50',
            field=models.DecimalField(null=True, verbose_name=b'0', max_digits=6, decimal_places=3),
        ),
    ]
