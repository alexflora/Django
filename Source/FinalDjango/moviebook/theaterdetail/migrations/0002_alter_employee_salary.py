# Generated by Django 3.2 on 2022-10-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theaterdetail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='salary',
            field=models.FloatField(null=True, verbose_name='Salary'),
        ),
    ]
