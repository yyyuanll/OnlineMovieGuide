# Generated by Django 4.0 on 2022-01-02 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('box_office', models.BigIntegerField(blank=True, db_column='Box_office', null=True)),
                ('country', models.CharField(blank=True, db_column='Country', max_length=255, null=True)),
                ('rated', models.CharField(blank=True, db_column='Rated', max_length=255, null=True)),
                ('imdbid', models.CharField(blank=True, db_column='imdbID', max_length=255, null=True)),
                ('awards', models.CharField(blank=True, db_column='Awards', max_length=255, null=True)),
                ('poster', models.CharField(blank=True, db_column='Poster', max_length=255, null=True)),
                ('director', models.CharField(blank=True, db_column='Director', max_length=1024, null=True)),
                ('released', models.CharField(blank=True, db_column='Released', max_length=255, null=True)),
                ('writer', models.CharField(blank=True, db_column='Writer', max_length=1024, null=True)),
                ('imdbvotes', models.IntegerField(blank=True, db_column='imdbVotes', null=True)),
                ('runtime', models.CharField(blank=True, db_column='Runtime', max_length=255, null=True)),
                ('imdbrating', models.FloatField(blank=True, db_column='imdbRating', null=True)),
                ('title', models.CharField(blank=True, db_column='Title', max_length=255, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('field_year', models.IntegerField(blank=True, db_column='_year', null=True)),
                ('field_month', models.IntegerField(blank=True, db_column='_month', null=True)),
                ('field_day', models.IntegerField(blank=True, db_column='_day', null=True)),
                ('metascore', models.IntegerField(blank=True, db_column='Metascore', null=True)),
                ('response', models.CharField(blank=True, db_column='Response', max_length=255, null=True)),
            ],
            options={
                'db_table': 'film',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('imdbid', models.CharField(blank=True, max_length=255, null=True)),
                ('genre', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'genre',
                'managed': False,
            },
        ),
    ]
