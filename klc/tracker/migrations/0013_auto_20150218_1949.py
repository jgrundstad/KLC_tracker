# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0012_auto_20150218_1939'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='contact',
            new_name='contacts',
        ),
    ]
