# Generated by Django 5.0.6 on 2024-05-30 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0002_employee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_name', models.CharField(max_length=200)),
                ('doc_spec', models.TextField()),
                ('doc_image', models.ImageField(default='default_image.jpg', upload_to='doctors')),
                ('department_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='units.department')),
            ],
        ),
        migrations.DeleteModel(
            name='Employee',
        ),
    ]
