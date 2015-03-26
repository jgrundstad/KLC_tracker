# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0013_auto_20150218_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
