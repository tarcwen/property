# Generated by Django 3.1 on 2023-11-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profileOTP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='otp_secret',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
