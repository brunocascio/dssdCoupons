# Generated by Django 2.1.2 on 2018-11-27 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20181025_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='discount',
            field=models.DecimalField(decimal_places=2, default=3.0, max_digits=5),
        ),
    ]
