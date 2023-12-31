# Generated by Django 3.1 on 2023-11-21 16:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0009_remove_realtor_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('listing', '0007_auto_20231118_1812'),
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='listing_id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
        migrations.AddField(
            model_name='contact',
            name='apptDateTime',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='contact',
            name='realtor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor'),
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.CharField(default='Pending', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contact',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='listing.listing'),
        ),
    ]
