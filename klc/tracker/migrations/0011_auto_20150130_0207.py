# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0010_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='code',
            name='value',
            field=models.TextField(max_length=512),
            preserve_default=True,
        ),
    ]
