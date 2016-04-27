# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('maji_sys', '0002_auto_20151027_0907'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dump',
            fields=[
                ('dump_id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField()),
                ('value', models.FloatField(blank=True)),
                ('parameterid', models.CharField(max_length=64, null=True, blank=True)),
                ('locationid', models.CharField(max_length=64, null=True, blank=True)),
                ('flag', models.IntegerField()),
                ('comment', models.CharField(max_length=64, blank=True)),
            ],
            options={
                'db_table': 'dump',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Submissions',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('parameter_id', models.CharField(max_length=64, blank=True)),
                ('value_entries', jsonfield.fields.JSONField()),
                ('location_id', models.CharField(max_length=64, blank=True)),
                ('unit', models.CharField(max_length=64, blank=True)),
            ],
            options={
                'db_table': 'submissions',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelTable(
            name='features',
            table='featureclass',
        ),
    ]
