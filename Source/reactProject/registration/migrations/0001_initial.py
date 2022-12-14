# Generated by Django 3.2 on 2022-09-19 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Country')),
                ('code', models.CharField(max_length=30, null=True, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('code', models.CharField(max_length=30, null=True, verbose_name='code')),
            ],
        ),
        migrations.CreateModel(
            name='personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('age', models.IntegerField(null=True, verbose_name='Age')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=30, null=True, verbose_name='Gender')),
                ('dob', models.DateField(null=True, verbose_name='DOB')),
                ('phone', models.IntegerField(null=True, verbose_name='Phone')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('pincode', models.IntegerField(blank=True, null=True, verbose_name='Pincode')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='registration.country', verbose_name='Country')),
            ],
        ),
    ]
