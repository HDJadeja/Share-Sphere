# Generated by Django 5.1.4 on 2025-01-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CCmembers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
    ]
