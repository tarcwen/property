# Generated by Django 3.1 on 2023-12-03 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20231203_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date_end',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contact_date_start',
            field=models.DateTimeField(blank=True),
        ),
    ]
