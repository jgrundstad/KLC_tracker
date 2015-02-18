# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_auto_20150130_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
