# Generated by Django 4.1 on 2022-09-06 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_article_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.DateField(blank=True, null=True),
        ),
    ]
