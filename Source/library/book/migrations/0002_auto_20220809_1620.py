# Generated by Django 3.2 on 2022-08-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='Name',
            field=models.CharField(max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(max_length=200, null=True, verbose_name='code'),
        ),
    ]
