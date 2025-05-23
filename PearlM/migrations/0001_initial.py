# Generated by Django 5.1.4 on 2025-01-16 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product_PMclub',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.DecimalField(decimal_places=5, max_digits=10)),
                ('product_monarch', models.CharField(max_length=50)),
                ('product_image', models.ImageField(upload_to='images')),
                ('product_country', models.CharField(max_length=30)),
            ],
        ),
    ]
