# Generated by Django 5.1.4 on 2025-02-02 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CCClub', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product_ccclub',
            name='art_img',
            field=models.ImageField(upload_to='CCClub/'),
        ),
    ]
