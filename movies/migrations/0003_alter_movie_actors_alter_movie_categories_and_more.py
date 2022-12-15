# Generated by Django 4.1.4 on 2022-12-15 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movies", "0002_rename_thumbnail_url_movie_thumb_url_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie",
            name="actors",
            field=models.ManyToManyField(blank=True, null=True, to="movies.actor"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="categories",
            field=models.ManyToManyField(blank=True, null=True, to="movies.category"),
        ),
        migrations.AlterField(
            model_name="movie",
            name="directors",
            field=models.ManyToManyField(blank=True, null=True, to="movies.director"),
        ),
    ]
