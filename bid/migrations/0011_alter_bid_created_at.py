# Generated by Django 3.2.3 on 2021-05-26 09:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0010_alter_bid_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 5, 26, 15, 54, 6, 802303)),
        ),
    ]
