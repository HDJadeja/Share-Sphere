# Generated by Django 5.1.4 on 2025-01-14 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSSS', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ssss_products',
            name='product_image',
            field=models.ImageField(default=0, upload_to='images'),
            preserve_default=False,
        ),
    ]
