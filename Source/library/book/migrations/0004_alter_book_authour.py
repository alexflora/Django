# Generated by Django 3.2 on 2022-08-09 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_authour'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authour',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, to='book.authour'),
        ),
    ]