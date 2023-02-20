# Generated by Django 4.1.2 on 2023-01-13 06:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer_percentage',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(70)]),
        ),
        migrations.AddField(
            model_name='product',
            name='original_price',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
