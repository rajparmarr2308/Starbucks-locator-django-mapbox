# Generated by Django 4.2 on 2023-04-28 16:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SB_app', '0002_alter_location_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='lat',
            field=models.CharField(default='null', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='long',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]