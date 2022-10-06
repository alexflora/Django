# Generated by Django 3.2 on 2022-09-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configration', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='state',
            old_name='test',
            new_name='country',
        ),
        migrations.AlterField(
            model_name='state',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='state',
            name='state',
            field=models.CharField(max_length=255, null=True, verbose_name='State'),
        ),
    ]