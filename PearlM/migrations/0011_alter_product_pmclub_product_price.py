# Generated by Django 5.1.4 on 2025-02-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PearlM', '0010_alter_product_pmclub_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_pmclub',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
