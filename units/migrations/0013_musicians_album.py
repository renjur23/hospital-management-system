# Generated by Django 5.0.6 on 2024-07-08 10:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0012_alter_pharmacy_med_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='musicians',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('instrument', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField(auto_now=True)),
                ('rating', models.IntegerField()),
                ('first_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.musicians')),
            ],
        ),
    ]
