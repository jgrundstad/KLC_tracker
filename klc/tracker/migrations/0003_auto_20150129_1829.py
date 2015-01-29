# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_client_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proceeding',
            name='name',
            field=models.CharField(max_length=128),
            preserve_default=True,
        ),
    ]
