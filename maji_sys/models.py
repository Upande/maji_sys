from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from jsonfield import JSONField


class Aggregationperiods(models.Model):
	aggregationperiodkey = models.IntegerField(primary_key=True)
	id = models.CharField(unique=True, max_length=64)
	description = models.CharField(max_length=255, blank=True)

	class Meta:
		managed = False
		db_table = 'aggregationperiods'

class Dump(models.Model):
    date = models.DateTimeField()
    value = models.FloatField(blank=True)
    parameterid = models.CharField(max_length=64, blank=True, null=True)
    locationid = models.CharField(max_length=64, blank=True, null=True)
    flag = models.IntegerField()
    comment = models.CharField(max_length=64, blank=True)

    class Meta:
        managed = False
        db_table = 'dump'

class Features(models.Model):
    featureclasskey = models.IntegerField(primary_key=True)
    featureclassname = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'featureclass'

class Filters(models.Model):
	filterkey = models.IntegerField(primary_key=True)
	id = models.CharField(unique=True, max_length=64)
	name = models.CharField(max_length=64, blank=True)
	description = models.CharField(max_length=255, blank=True)
	parentfilterid = models.CharField(max_length=64, blank=True)
	validationiconsvisible = models.IntegerField()
	mapextentid = models.CharField(max_length=64, blank=True)
	viewpermission = models.CharField(max_length=64, blank=True)
	editpermission = models.CharField(max_length=64, blank=True)

	class Meta:
		managed = False
		db_table = 'filters'


class Filtertimeserieskeys(models.Model):
	filterkey = models.ForeignKey(Filters, db_column='filterkey')
	serieskey = models.ForeignKey('Timeserieskeys', db_column='serieskey')

	class Meta:
		managed = False
		db_table = 'filtertimeserieskeys'


class Parametergroups(models.Model):
	groupkey = models.IntegerField(primary_key=True)
	id = models.CharField(unique=True, max_length=64)
	name = models.CharField(max_length=64, blank=True)
	description = models.CharField(max_length=255, blank=True)
	parametertype = models.CharField(max_length=64)
	unit = models.CharField(max_length=64, blank=True)
	displayunit = models.CharField(max_length=64, blank=True)
        

	class Meta:
		managed = False
		db_table = 'parametergroups'


class Parameterstable(models.Model):
	parameterkey = models.IntegerField(primary_key=True)
	groupkey = models.ForeignKey(Parametergroups, db_column='groupkey')
	id = models.CharField(unique=True, max_length=64)
	name = models.CharField(max_length=64, blank=True)
	shortname = models.CharField(max_length=64, blank=True)
	description = models.CharField(max_length=255, blank=True)
	valueresolution = models.FloatField(blank=True, null=True)
	attributea = models.CharField(max_length=64, blank=True)
	attributeb = models.FloatField(blank=True, null=True)
        featureclasskey = models.ForeignKey(Features, db_column='featureclasskey')
        #featuresclasskey = models.IntegerField(blank=True, null=True)
	class Meta:
                managed = False
                db_table = 'parameterstable'


class Locations(models.Model):
	locationkey = models.IntegerField(primary_key=True)
	id = models.CharField(unique=True, max_length=64)
	name = models.CharField(max_length=64, blank=True)
	shortname = models.CharField(max_length=64, blank=True)
	description = models.CharField(max_length=255, blank=True)
	icon = models.CharField(max_length=64, blank=True)
	tooltip = models.CharField(max_length=64, blank=True)
	parentlocationid = models.CharField(max_length=64, blank=True)
	visibilitystarttime = models.DateTimeField(blank=True, null=True)
	visibilityendtime = models.DateTimeField(blank=True, null=True)
	x = models.FloatField()
	y = models.FloatField()
	z = models.FloatField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'locations'


class GeographyColumns(models.Model):
    f_table_catalog = models.TextField(blank=True)  # This field type is a guess.
    f_table_schema = models.TextField(blank=True)  # This field type is a guess.
    f_table_name = models.TextField(blank=True)  # This field type is a guess.
    f_geography_column = models.TextField(blank=True)  # This field type is a guess.
    coord_dimension = models.IntegerField(blank=True, null=True)
    srid = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'geography_columns'


class GeometryColumns(models.Model):
    f_table_catalog = models.CharField(max_length=256, blank=True)
    f_table_schema = models.CharField(max_length=256, blank=True)
    f_table_name = models.CharField(max_length=256, blank=True)
    f_geometry_column = models.CharField(max_length=256, blank=True)
    coord_dimension = models.IntegerField(blank=True, null=True)
    srid = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'geometry_columns'


class Layer(models.Model):
    topology = models.ForeignKey('Topology')
    layer_id = models.IntegerField()
    schema_name = models.CharField(max_length=1)
    table_name = models.CharField(max_length=1)
    feature_column = models.CharField(max_length=1)
    feature_type = models.IntegerField()
    level = models.IntegerField()
    child_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'layer'


class Moduleinstances(models.Model):
    moduleinstancekey = models.IntegerField(primary_key=True)
    id = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'moduleinstances'


class Qualifiers(models.Model):
    qualifierkey = models.IntegerField(primary_key=True)
    id = models.CharField(unique=True, max_length=64)
    name = models.CharField(max_length=64, blank=True)
    shortname = models.CharField(max_length=64, blank=True)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'qualifiers'


class Qualifiersets(models.Model):
    qualifiersetkey = models.IntegerField(primary_key=True)
    id = models.CharField(unique=True, max_length=64)
    qualifierkey1 = models.ForeignKey(Qualifiers, db_column='qualifierkey1')

    class Meta:
        managed = False
        db_table = 'qualifiersets'


class RasterColumns(models.Model):
    r_table_catalog = models.TextField(blank=True)  # This field type is a guess.
    r_table_schema = models.TextField(blank=True)  # This field type is a guess.
    r_table_name = models.TextField(blank=True)  # This field type is a guess.
    r_raster_column = models.TextField(blank=True)  # This field type is a guess.
    srid = models.IntegerField(blank=True, null=True)
    scale_x = models.FloatField(blank=True, null=True)
    scale_y = models.FloatField(blank=True, null=True)
    blocksize_x = models.IntegerField(blank=True, null=True)
    blocksize_y = models.IntegerField(blank=True, null=True)
    same_alignment = models.NullBooleanField()
    regular_blocking = models.NullBooleanField()
    num_bands = models.IntegerField(blank=True, null=True)
    pixel_types = models.TextField(blank=True)  # This field type is a guess.
    nodata_values = models.TextField(blank=True)  # This field type is a guess.
    out_db = models.TextField(blank=True)  # This field type is a guess.
    extent = models.TextField(blank=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'raster_columns'


class RasterOverviews(models.Model):
    o_table_catalog = models.TextField(blank=True)  # This field type is a guess.
    o_table_schema = models.TextField(blank=True)  # This field type is a guess.
    o_table_name = models.TextField(blank=True)  # This field type is a guess.
    o_raster_column = models.TextField(blank=True)  # This field type is a guess.
    r_table_catalog = models.TextField(blank=True)  # This field type is a guess.
    r_table_schema = models.TextField(blank=True)  # This field type is a guess.
    r_table_name = models.TextField(blank=True)  # This field type is a guess.
    r_raster_column = models.TextField(blank=True)  # This field type is a guess.
    overview_factor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'raster_overviews'


class Samples(models.Model):
    locationkey = models.IntegerField()
    datetime = models.DateTimeField()
    identifier = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'samples'


class SpatialRefSys(models.Model):
    srid = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=256, blank=True)
    auth_srid = models.IntegerField(blank=True, null=True)
    srtext = models.CharField(max_length=2048, blank=True)
    proj4text = models.CharField(max_length=2048, blank=True)

    class Meta:
        managed = False
        db_table = 'spatial_ref_sys'

class Submissions(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    parameter_id = models.CharField(max_length=64, blank=True)
    value_entries = JSONField()
    location_id = models.CharField(max_length=64, blank=True)
    unit = models.CharField(max_length=64, blank=True)

    class Meta:
        managed = False
        db_table = 'submissions'
        


class Timeseriescomments(models.Model):
    serieskey = models.ForeignKey('Timeserieskeys', db_column='serieskey')
    datetime = models.DateTimeField()
    commenttext = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'timeseriescomments'


class Timeserieskeys(models.Model):
    serieskey = models.IntegerField(primary_key=True)
    locationkey = models.IntegerField()
    parameterkey = models.ForeignKey(Parameterstable, db_column='parameterkey')
    qualifiersetkey = models.ForeignKey(Qualifiersets, db_column='qualifiersetkey', blank=True, null=True)
    moduleinstancekey = models.ForeignKey(Moduleinstances, db_column='moduleinstancekey')
    timestepkey = models.ForeignKey('Timesteps', db_column='timestepkey')
    aggregationperiodkey = models.ForeignKey(Aggregationperiods, db_column='aggregationperiodkey', blank=True, null=True)
    valuetype = models.IntegerField()
    modificationtime = models.DateTimeField()
    featureclasskey = models.ForeignKey(Features, db_column='featureclasskey')

    class Meta:
        managed = False
        db_table = 'timeserieskeys'


class Timeseriesmanualeditshistory(models.Model):
    serieskey = models.ForeignKey(Timeserieskeys, db_column='serieskey')
    editdatetime = models.DateTimeField()
    datetime = models.DateTimeField()
    #userkey = models.ForeignKey(User, db_column='userkey', blank=True, null=True)
    userkey = models.IntegerField()
    scalarvalue = models.FloatField(blank=True, null=True)
    flags = models.IntegerField()
    commenttext = models.CharField(max_length=64, blank=True)

    class Meta:
        managed = False
        db_table = 'timeseriesmanualeditshistory'


class Timeseriesvaluesandflags(models.Model):
    serieskey = models.ForeignKey(Timeserieskeys, db_column='serieskey')
    datetime = models.DateTimeField()
    scalarvalue = models.FloatField(blank=True, null=True)
    flags = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'timeseriesvaluesandflags'


class Timesteps(models.Model):
    timestepkey = models.IntegerField(primary_key=True)
    id = models.CharField(unique=True, max_length=64)
    label = models.CharField(max_length=64, blank=True)

    class Meta:
        managed = False
        db_table = 'timesteps'


class Topology(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=10)
    srid = models.IntegerField()
    precision = models.FloatField()
    hasz = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'topology'
