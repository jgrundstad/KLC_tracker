# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0008_auto_20150130_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='role',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='client',
            name='short_name',
            field=models.CharField(default='', max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
