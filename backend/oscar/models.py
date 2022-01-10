# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from sqlalchemy import true


class Actor(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    actor = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actor'


class BestActor(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    year = models.ForeignKey('BestPicture', models.DO_NOTHING, db_column='year', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    profile = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    representitive = models.CharField(max_length=255, blank=True, null=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    character_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'best_actor'


class BestActress(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    year = models.ForeignKey('BestPicture', models.DO_NOTHING, db_column='year', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    profile = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    representitive = models.CharField(max_length=255, blank=True, null=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    character_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'best_actress'


class BestPicture(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    introduction = models.TextField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    runtime = models.CharField(max_length=255, blank=True, null=True)
    genre1 = models.CharField(max_length=255, blank=True, null=True)
    genre2 = models.CharField(max_length=255, blank=True, null=True)
    genre3 = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    star1 = models.CharField(max_length=255, blank=True, null=True)
    star2 = models.CharField(max_length=255, blank=True, null=True)
    star3 = models.CharField(max_length=255, blank=True, null=True)
    star4 = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    cover = models.CharField(max_length=255, blank=True, null=True)
    certificate = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'best_picture'


class BestSupportingActor(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    year = models.ForeignKey(BestPicture, models.DO_NOTHING, db_column='year', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    profile = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    representitive = models.CharField(max_length=255, blank=True, null=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    character_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'best_supporting_actor'


class BestSupportingActress(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    year = models.ForeignKey(BestPicture, models.DO_NOTHING, db_column='year', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    profile = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    representitive = models.CharField(max_length=255, blank=True, null=True)
    movie_name = models.CharField(max_length=255, blank=True, null=True)
    character_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'best_supporting_actress'