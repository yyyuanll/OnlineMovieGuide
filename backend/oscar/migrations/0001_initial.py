# Generated by Django 4.0 on 2021-12-19 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('movie', models.CharField(blank=True, max_length=255, null=True)),
                ('actor', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BestActor',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('profile', models.CharField(blank=True, max_length=255, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('representitive', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
                ('character_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'best_actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BestActress',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('profile', models.CharField(blank=True, max_length=255, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('representitive', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
                ('character_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'best_actress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BestPicture',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('runtime', models.CharField(blank=True, max_length=255, null=True)),
                ('genre1', models.CharField(blank=True, max_length=255, null=True)),
                ('genre2', models.CharField(blank=True, max_length=255, null=True)),
                ('genre3', models.CharField(blank=True, max_length=255, null=True)),
                ('director', models.CharField(blank=True, max_length=255, null=True)),
                ('star1', models.CharField(blank=True, max_length=255, null=True)),
                ('star2', models.CharField(blank=True, max_length=255, null=True)),
                ('star3', models.CharField(blank=True, max_length=255, null=True)),
                ('star4', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('cover', models.CharField(blank=True, max_length=255, null=True)),
                ('certificate', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'best_picture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BestSupportingActor',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('profile', models.CharField(blank=True, max_length=255, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('representitive', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
                ('character_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'best_supporting_actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BestSupportingActress',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('link', models.CharField(blank=True, max_length=255, null=True)),
                ('profile', models.CharField(blank=True, max_length=255, null=True)),
                ('introduction', models.TextField(blank=True, null=True)),
                ('representitive', models.CharField(blank=True, max_length=255, null=True)),
                ('movie_name', models.CharField(blank=True, max_length=255, null=True)),
                ('character_name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'best_supporting_actress',
                'managed': False,
            },
        ),
    ]
