# Generated by Django 4.0 on 2021-12-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_delete_favorite_delete_history_delete_review_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('field_id', models.IntegerField(db_column='_id', primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=255, null=True)),
                ('movie', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'favorite',
                'managed': False,
            },
        ),
    ]