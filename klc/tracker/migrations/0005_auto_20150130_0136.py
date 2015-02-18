# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20150129_1836'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='time_spent',
            new_name='minutes_spent',
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(help_text=b'doing', max_length=128),
            preserve_default=True,
        ),
    ]
