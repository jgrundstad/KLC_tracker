# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_auto_20150130_0207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128, blank=True)),
                ('last_name', models.CharField(max_length=128, blank=True)),
                ('short_name', models.CharField(max_length=32, blank=True)),
                ('role', models.CharField(max_length=128, blank=True)),
                ('company', models.CharField(max_length=128, blank=True)),
                ('address1', models.CharField(max_length=128, blank=True)),
                ('address2', models.CharField(max_length=128, blank=True)),
                ('city', models.CharField(max_length=64, blank=True)),
                ('state', models.CharField(max_length=16, blank=True)),
                ('zipcode', models.CharField(max_length=12, blank=True)),
                ('phone1', models.CharField(max_length=24, blank=True)),
                ('phone2', models.CharField(max_length=24, blank=True)),
                ('fax', models.CharField(max_length=24, blank=True)),
                ('email', models.EmailField(max_length=128, blank=True)),
                ('comment', models.TextField(blank=b'True')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='proceeding',
            name='client',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.AddField(
            model_name='item',
            name='contact',
            field=models.ManyToManyField(to='tracker.Contact'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='proceeding',
            name='contact',
            field=models.ForeignKey(default=1, to='tracker.Contact'),
            preserve_default=False,
        ),
    ]
