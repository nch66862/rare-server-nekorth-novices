# Generated by Django 3.2.3 on 2021-05-17 16:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rareapi', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rareuser',
            name='active',
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 17, 16, 25, 20, 859099, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='publication_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 17, 16, 25, 20, 860888, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rareuser',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 17, 16, 25, 20, 862018, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created_on',
            field=models.DateField(default=datetime.datetime(2021, 5, 17, 16, 25, 20, 864177, tzinfo=utc)),
        ),
    ]
