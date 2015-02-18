# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_auto_20150130_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='minutes_spent',
        ),
        migrations.AddField(
            model_name='item',
            name='notes',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
