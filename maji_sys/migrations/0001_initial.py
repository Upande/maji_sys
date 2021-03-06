# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aggregationperiods',
            fields=[
                ('aggregationperiodkey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'aggregationperiods',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('featureclasskey', models.IntegerField(serialize=False, primary_key=True)),
                ('featureclass', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'feature_class',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filters',
            fields=[
                ('filterkey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(max_length=64, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('parentfilterid', models.CharField(max_length=64, blank=True)),
                ('validationiconsvisible', models.IntegerField()),
                ('mapextentid', models.CharField(max_length=64, blank=True)),
                ('viewpermission', models.CharField(max_length=64, blank=True)),
                ('editpermission', models.CharField(max_length=64, blank=True)),
            ],
            options={
                'db_table': 'filters',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Filtertimeserieskeys',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'db_table': 'filtertimeserieskeys',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeographyColumns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_table_catalog', models.TextField(blank=True)),
                ('f_table_schema', models.TextField(blank=True)),
                ('f_table_name', models.TextField(blank=True)),
                ('f_geography_column', models.TextField(blank=True)),
                ('coord_dimension', models.IntegerField(null=True, blank=True)),
                ('srid', models.IntegerField(null=True, blank=True)),
                ('type', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'geography_columns',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeometryColumns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_table_catalog', models.CharField(max_length=256, blank=True)),
                ('f_table_schema', models.CharField(max_length=256, blank=True)),
                ('f_table_name', models.CharField(max_length=256, blank=True)),
                ('f_geometry_column', models.CharField(max_length=256, blank=True)),
                ('coord_dimension', models.IntegerField(null=True, blank=True)),
                ('srid', models.IntegerField(null=True, blank=True)),
                ('type', models.CharField(max_length=30, blank=True)),
            ],
            options={
                'db_table': 'geometry_columns',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Layer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('layer_id', models.IntegerField()),
                ('schema_name', models.CharField(max_length=1)),
                ('table_name', models.CharField(max_length=1)),
                ('feature_column', models.CharField(max_length=1)),
                ('feature_type', models.IntegerField()),
                ('level', models.IntegerField()),
                ('child_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'layer',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Locations',
            fields=[
                ('locationkey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(max_length=64, blank=True)),
                ('shortname', models.CharField(max_length=64, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('icon', models.CharField(max_length=64, blank=True)),
                ('tooltip', models.CharField(max_length=64, blank=True)),
                ('parentlocationid', models.CharField(max_length=64, blank=True)),
                ('visibilitystarttime', models.DateTimeField(null=True, blank=True)),
                ('visibilityendtime', models.DateTimeField(null=True, blank=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField(null=True, blank=True)),
                ('wgs_geom', models.TextField(blank=True)),
                ('area', models.FloatField(null=True, blank=True)),
                ('relationalocationid', models.CharField(max_length=64, blank=True)),
                ('relationblocationid', models.CharField(max_length=64, blank=True)),
                ('attributea', models.CharField(max_length=64, blank=True)),
                ('attributeb', models.FloatField(null=True, blank=True)),
                ('rainfall', models.NullBooleanField()),
                ('lake_level', models.CharField(max_length=1, blank=True)),
                ('harmax_h', models.FloatField(null=True, blank=True)),
                ('harmin_h', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'locations',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Moduleinstances',
            fields=[
                ('moduleinstancekey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(max_length=64, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'moduleinstances',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parametergroups',
            fields=[
                ('groupkey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(max_length=64, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('parametertype', models.CharField(max_length=64)),
                ('unit', models.CharField(max_length=64, blank=True)),
                ('displayunit', models.CharField(max_length=64, blank=True)),
            ],
            options={
                'db_table': 'parametergroups',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parameterstable',
            fields=[
                ('parameterkey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(max_length=64, blank=True)),
                ('shortname', models.CharField(max_length=64, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('valueresolution', models.FloatField(null=True, blank=True)),
                ('attributea', models.CharField(max_length=64, blank=True)),
                ('attributeb', models.FloatField(null=True, blank=True)),
            ],
            options={
                'db_table': 'parameterstable',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Qualifiers',
            fields=[
                ('qualifierkey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
                ('name', models.CharField(max_length=64, blank=True)),
                ('shortname', models.CharField(max_length=64, blank=True)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'qualifiers',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Qualifiersets',
            fields=[
                ('qualifiersetkey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
            ],
            options={
                'db_table': 'qualifiersets',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RasterColumns',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('r_table_catalog', models.TextField(blank=True)),
                ('r_table_schema', models.TextField(blank=True)),
                ('r_table_name', models.TextField(blank=True)),
                ('r_raster_column', models.TextField(blank=True)),
                ('srid', models.IntegerField(null=True, blank=True)),
                ('scale_x', models.FloatField(null=True, blank=True)),
                ('scale_y', models.FloatField(null=True, blank=True)),
                ('blocksize_x', models.IntegerField(null=True, blank=True)),
                ('blocksize_y', models.IntegerField(null=True, blank=True)),
                ('same_alignment', models.NullBooleanField()),
                ('regular_blocking', models.NullBooleanField()),
                ('num_bands', models.IntegerField(null=True, blank=True)),
                ('pixel_types', models.TextField(blank=True)),
                ('nodata_values', models.TextField(blank=True)),
                ('out_db', models.TextField(blank=True)),
                ('extent', models.TextField(blank=True)),
            ],
            options={
                'db_table': 'raster_columns',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RasterOverviews',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('o_table_catalog', models.TextField(blank=True)),
                ('o_table_schema', models.TextField(blank=True)),
                ('o_table_name', models.TextField(blank=True)),
                ('o_raster_column', models.TextField(blank=True)),
                ('r_table_catalog', models.TextField(blank=True)),
                ('r_table_schema', models.TextField(blank=True)),
                ('r_table_name', models.TextField(blank=True)),
                ('r_raster_column', models.TextField(blank=True)),
                ('overview_factor', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'raster_overviews',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Samples',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('locationkey', models.IntegerField()),
                ('datetime', models.DateTimeField()),
                ('identifier', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'samples',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SpatialRefSys',
            fields=[
                ('srid', models.IntegerField(serialize=False, primary_key=True)),
                ('auth_name', models.CharField(max_length=256, blank=True)),
                ('auth_srid', models.IntegerField(null=True, blank=True)),
                ('srtext', models.CharField(max_length=2048, blank=True)),
                ('proj4text', models.CharField(max_length=2048, blank=True)),
            ],
            options={
                'db_table': 'spatial_ref_sys',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timeseriescomments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('commenttext', models.CharField(max_length=64)),
            ],
            options={
                'db_table': 'timeseriescomments',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timeserieskeys',
            fields=[
                ('serieskey', models.IntegerField(serialize=False, primary_key=True)),
                ('locationkey', models.IntegerField()),
                ('valuetype', models.IntegerField()),
                ('modificationtime', models.DateTimeField()),
            ],
            options={
                'db_table': 'timeserieskeys',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timeseriesmanualeditshistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('editdatetime', models.DateTimeField()),
                ('datetime', models.DateTimeField()),
                ('userkey', models.IntegerField()),
                ('scalarvalue', models.FloatField(null=True, blank=True)),
                ('flags', models.IntegerField()),
                ('commenttext', models.CharField(max_length=64, blank=True)),
            ],
            options={
                'db_table': 'timeseriesmanualeditshistory',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timeseriesvaluesandflags',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('datetime', models.DateTimeField()),
                ('scalarvalue', models.FloatField(null=True, blank=True)),
                ('flags', models.IntegerField()),
            ],
            options={
                'db_table': 'timeseriesvaluesandflags',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Timesteps',
            fields=[
                ('timestepkey', models.IntegerField(serialize=False, primary_key=True)),
                ('id', models.CharField(unique=True, max_length=64)),
                ('label', models.CharField(max_length=64, blank=True)),
            ],
            options={
                'db_table': 'timesteps',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Topology',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=10)),
                ('srid', models.IntegerField()),
                ('precision', models.FloatField()),
                ('hasz', models.BooleanField()),
            ],
            options={
                'db_table': 'topology',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
