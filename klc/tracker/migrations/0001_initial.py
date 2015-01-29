# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('company', models.CharField(max_length=128, blank=True)),
                ('address1', models.CharField(max_length=128, blank=True)),
                ('address2', models.CharField(max_length=128, blank=True)),
                ('city', models.CharField(max_length=64, blank=True)),
                ('state', models.CharField(max_length=16, blank=True)),
                ('phone1', models.CharField(max_length=24, blank=True)),
                ('phone2', models.CharField(max_length=24, blank=True)),
                ('fax', models.CharField(max_length=24, blank=True)),
                ('email', models.CharField(max_length=128, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=256)),
                ('date', models.DateTimeField()),
                ('time_spent', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Proceeding',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=1)),
                ('start_date', models.DateTimeField()),
                ('archive', models.CharField(default=b'N', max_length=1, choices=[(b'Y', b'Y'), (b'N', b'N')])),
                ('client', models.ForeignKey(to='tracker.Client')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='item',
            name='proceeding',
            field=models.ForeignKey(to='tracker.Proceeding'),
            preserve_default=True,
        ),
    ]
