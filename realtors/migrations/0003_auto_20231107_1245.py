# Generated by Django 3.1 on 2023-11-07 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0002_realtor_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(default='/image/noIMG.png', upload_to='photos/%Y/%m/%d/'),
        ),
    ]
