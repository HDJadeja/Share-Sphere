# Generated by Django 5.1.4 on 2025-01-19 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SSMAIN', '0004_members_invited_invited_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='admins',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_id', models.CharField(max_length=20)),
                ('admin_pass', models.CharField(max_length=20)),
            ],
        ),
    ]
