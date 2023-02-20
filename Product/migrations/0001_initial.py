# Generated by Django 4.1.2 on 2023-01-08 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prdct_name', models.CharField(max_length=500, unique=True)),
                ('prdct_desc', models.TextField(blank=True, max_length=500)),
                ('slug', models.SlugField(max_length=500, unique=True)),
                ('price', models.FloatField()),
                ('stock', models.BigIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('img1', models.ImageField(blank=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, upload_to='images/')),
                ('img4', models.ImageField(blank=True, upload_to='images/')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Category.category')),
                ('subcategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Category.subcategory')),
            ],
        ),
    ]