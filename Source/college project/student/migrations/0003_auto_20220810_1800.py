# Generated by Django 3.2 on 2022-08-10 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20220810_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='datetime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
