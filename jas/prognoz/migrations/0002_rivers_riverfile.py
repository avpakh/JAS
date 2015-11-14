# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prognoz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rivers',
            name='riverfile',
            field=models.TextField(default=1, verbose_name=b'\xd0\xa4\xd0\xb0\xd0\xb9\xd0\xbb \xd1\x80\xd0\xb5\xd0\xba\xd0\xb8'),
            preserve_default=False,
        ),
    ]
