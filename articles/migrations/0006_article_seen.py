# Generated by Django 4.0.1 on 2022-01-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_comment_article_alter_comment_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='seen',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
