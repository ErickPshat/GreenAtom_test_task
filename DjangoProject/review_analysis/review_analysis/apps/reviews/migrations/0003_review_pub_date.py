# Generated by Django 3.0.7 on 2020-06-23 20:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20200623_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 23, 20, 11, 20, 409022, tzinfo=utc), verbose_name='date of the review'),
            preserve_default=False,
        ),
    ]
