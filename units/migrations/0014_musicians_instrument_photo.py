# Generated by Django 5.0.6 on 2024-07-08 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0013_musicians_album'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicians',
            name='instrument_photo',
            field=models.ImageField(blank=True, null=True, upload_to='instrument_photos/'),
        ),
    ]
