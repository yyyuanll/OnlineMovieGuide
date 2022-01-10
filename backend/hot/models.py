# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from sqlalchemy import true
from user.models import History

class Film(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    box_office = models.BigIntegerField(db_column='Box_office', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rated = models.CharField(db_column='Rated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imdbid = models.CharField(db_column='imdbID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    awards = models.CharField(db_column='Awards', max_length=255, blank=True, null=True)  # Field name made lowercase.
    poster = models.CharField(db_column='Poster', max_length=255, blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    writer = models.CharField(db_column='Writer', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    imdbvotes = models.IntegerField(db_column='imdbVotes', blank=True, null=True)  # Field name made lowercase.
    runtime = models.CharField(db_column='Runtime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imdbrating = models.FloatField(db_column='imdbRating', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    metascore = models.IntegerField(db_column='Metascore', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True, null=True)
    field_year = models.IntegerField(db_column='_year', blank=True, null=True)  # Field renamed because it started with '_'.
    field_month = models.IntegerField(db_column='_month', blank=True, null=True)  # Field renamed because it started with '_'.
    field_day = models.IntegerField(db_column='_day', blank=True, null=True)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'film'