# Generated by Django 4.1.2 on 2023-01-09 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Order', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='payment',
        ),
        migrations.AddField(
            model_name='order',
            name='is_orderd',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_id',
            field=models.CharField(default=0, max_length=200),
        ),
        migrations.AddField(
            model_name='order',
            name='payment_mode',
            field=models.CharField(default='Pending', max_length=200),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='is_ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='order_number',
            field=models.CharField(default=1, max_length=20),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Placed', 'Placed'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Placed', max_length=100),
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
