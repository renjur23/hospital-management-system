# Generated by Django 5.0.6 on 2024-05-29 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('units', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('emp_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Emp_name', models.CharField(max_length=50, verbose_name='Employee_Name')),
                ('Emp_age', models.IntegerField(verbose_name='Employee_Age')),
                ('Emp_Designation', models.CharField(max_length=50, verbose_name='Employee_Designation')),
                ('Emp_salary', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Employee_salary')),
            ],
        ),
    ]
