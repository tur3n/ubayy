# Generated by Django 3.2.3 on 2021-05-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0007_alter_product_minimum_bid_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
