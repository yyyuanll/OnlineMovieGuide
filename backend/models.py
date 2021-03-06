# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actor(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    actor = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actor'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BestActor(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    year = models.IntegerField(blank=True, null=True)
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
    year = models.IntegerField(blank=True, null=True)
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
    year = models.IntegerField(blank=True, null=True)
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
    year = models.IntegerField(blank=True, null=True)
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


class Country(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    imdb_country = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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


class Language(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    language = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'language'


class Review(models.Model):
    field_id = models.IntegerField(db_column='_id', primary_key=True)  # Field renamed because it started with '_'.
    imdbid = models.CharField(max_length=255, blank=True, null=True)
    movie = models.CharField(max_length=255, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    star = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'review'


class UserEmailverifyrecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    code = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    send_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_emailverifyrecord'


class Username(models.Model):
    username = models.CharField(primary_key=True, max_length=255)
    password = models.TextField()
    mail = models.CharField(max_length=255, blank=True, null=True)
    head_portrait = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'username'
