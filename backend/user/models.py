from django.db import models

class Country(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    imdb_country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class Favorite(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    username = models.CharField(max_length=255, blank=True, null=True)
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    movie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'favorite'


class Film(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    box_office = models.BigIntegerField(db_column='Box_office', blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    rated = models.CharField(db_column='Rated', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imdbid = models.CharField(db_column='imdbID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    awards = models.CharField(db_column='Awards', max_length=255, blank=True, null=True)  # Field name made lowercase.
    poster = models.CharField(db_column='Poster', max_length=255, blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='Director', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    released = models.CharField(db_column='Released', max_length=255, blank=True, null=True)  # Field name made lowercase.
    writer = models.CharField(db_column='Writer', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    imdbvotes = models.IntegerField(db_column='imdbVotes', blank=True, null=True)  # Field name made lowercase.
    runtime = models.CharField(db_column='Runtime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    imdbrating = models.FloatField(db_column='imdbRating', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=255, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=255, blank=True, null=True)
    field_year = models.IntegerField(db_column='_year', blank=True, null=True)  # Field renamed because it started with '_'.
    field_month = models.IntegerField(db_column='_month', blank=True, null=True)  # Field renamed because it started with '_'.
    field_day = models.IntegerField(db_column='_day', blank=True, null=True)  # Field renamed because it started with '_'.
    metascore = models.IntegerField(db_column='Metascore', blank=True, null=True)  # Field name made lowercase.
    response = models.CharField(db_column='Response', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'film'


class Genre(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    genre = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genre'


class History(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    username = models.CharField(max_length=255, blank=True, null=True)
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    movie = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'history'


class Review(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    username = models.CharField(max_length=255, blank=True, null=True)
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    movie = models.CharField(max_length=255, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class Username(models.Model):
    username = models.CharField(max_length=255,primary_key=True)
    password = models.TextField()
    mail = models.CharField(max_length=255, blank=True, null=True)
    head_portrait = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'username'