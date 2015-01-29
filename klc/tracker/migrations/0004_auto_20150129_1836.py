# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20150129_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='time_spent',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
