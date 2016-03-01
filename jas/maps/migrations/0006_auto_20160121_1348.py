# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0005_probability'),
    ]

    operations = [
        migrations.CreateModel(
            name='MapImage',
            fields=[
                ('id_mapimage', models.AutoField(serialize=False, primary_key=True)),
                ('map_image', sorl.thumbnail.fields.ImageField(upload_to=b'maps/static/im/')),
            ],
            options={
                'db_table': 'MapImage',
                'managed': True,
            },
        ),
        migrations.AlterModelOptions(
            name='probability',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='probability',
            table='Probability',
        ),
        migrations.AddField(
            model_name='mapimage',
            name='prob_index',
            field=models.ForeignKey(to='maps.Probability'),
        ),
        migrations.AddField(
            model_name='mapimage',
            name='rvb_index',
            field=models.ForeignKey(to='maps.RiverBasin'),
        ),
        migrations.AddField(
            model_name='mapimage',
            name='typm_index',
            field=models.ForeignKey(to='maps.TypeMap'),
        ),
    ]
