# Generated by Django 2.1.2 on 2018-11-28 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_coupon_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount',
            field=models.IntegerField(default=10),
        ),
    ]