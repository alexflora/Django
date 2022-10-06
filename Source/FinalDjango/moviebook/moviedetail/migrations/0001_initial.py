# Generated by Django 3.2 on 2022-10-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='Language')),
            ],
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='ShowName')),
                ('starttime', models.TimeField(null=True, verbose_name='Starttime')),
                ('endtime', models.TimeField(null=True, verbose_name='EndTime')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='MovieName')),
                ('actor', models.CharField(max_length=100, null=True, verbose_name='ActorName')),
                ('startdate', models.DateField(null=True, verbose_name='StartDate')),
                ('enddate', models.DateField(blank=True, null=True, verbose_name='EndDate')),
                ('movieimage', models.ImageField(null=True, upload_to='media/picture/')),
                ('language', models.ManyToManyField(to='moviedetail.Language')),
                ('show', models.ManyToManyField(to='moviedetail.Show')),
            ],
        ),
    ]