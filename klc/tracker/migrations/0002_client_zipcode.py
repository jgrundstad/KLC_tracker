# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='zipcode',
            field=models.CharField(max_length=12, blank=True),
            preserve_default=True,
        ),
    ]
