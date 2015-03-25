from __future__ import unicode_literals

from django.db import models

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
	wgs_geom = models.TextField(blank=True)  # This field type is a guess.
	area = models.FloatField(blank=True, null=True)
	relationalocationid = models.CharField(max_length=64, blank=True)
	relationblocationid = models.CharField(max_length=64, blank=True)
	attributea = models.CharField(max_length=64, blank=True)
	attributeb = models.FloatField(blank=True, null=True)
	rainfall = models.NullBooleanField()
	lake_level = models.CharField(max_length=1, blank=True)
	harmax_h = models.FloatField(blank=True, null=True)
	harmin_h = models.FloatField(blank=True, null=True)

	class Meta:
		managed = False
		db_table = 'locations'
