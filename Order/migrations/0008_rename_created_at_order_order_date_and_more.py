# Generated by Django 4.1.2 on 2023-01-17 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0007_alter_order_order_day'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_at',
            new_name='order_date',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Order_day',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Order_month',
        ),
        migrations.RemoveField(
            model_name='order',
            name='Order_year',
        ),
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated_at',
        ),
    ]