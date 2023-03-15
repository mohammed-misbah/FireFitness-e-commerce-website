# Generated by Django 4.1.2 on 2023-02-28 04:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Product', '0001_initial'),
        ('Cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12, unique=True)),
                ('email', models.CharField(max_length=100)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('dist', models.CharField(max_length=100)),
                ('pincode', models.IntegerField()),
                ('order_note', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=20)),
                ('payment_mode', models.CharField(default='Pending', max_length=200)),
                ('payment_id', models.CharField(default=0, max_length=200)),
                ('status', models.CharField(choices=[('Placed', 'Placed'), ('Shipped', 'Shipped'), ('Out For Delivery', 'Out For Delivery'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Placed', max_length=100)),
                ('order_total', models.FloatField()),
                ('tax', models.FloatField()),
                ('is_orderd', models.BooleanField(default=False)),
                ('Order_day', models.IntegerField(default=28)),
                ('Order_month', models.IntegerField(default=2)),
                ('Order_year', models.IntegerField(default=2023)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(default=1, max_length=20)),
                ('quantity', models.IntegerField()),
                ('product_price', models.FloatField()),
                ('is_ordered', models.BooleanField(default=False)),
                ('ordered', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('variation', models.ManyToManyField(blank=True, to='Cart.variation')),
            ],
        ),
    ]
