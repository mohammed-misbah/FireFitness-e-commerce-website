# Generated by Django 4.1.2 on 2023-01-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0004_order_order_day_order_order_month_order_order_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='Order_day',
            field=models.IntegerField(default=12),
        ),
    ]
