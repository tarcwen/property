# Generated by Django 3.1 on 2023-11-27 06:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0002_auto_20231121_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]