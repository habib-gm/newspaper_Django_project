# Generated by Django 4.0.1 on 2022-01-06 19:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0008_alter_article_saw_users_alter_article_seen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='saw_users',
            field=models.ManyToManyField(related_name='saw_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
