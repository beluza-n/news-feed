# Generated by Django 5.0.6 on 2024-05-11 08:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_favorites_favorites_unique_news'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='publication date'),
        ),
    ]
