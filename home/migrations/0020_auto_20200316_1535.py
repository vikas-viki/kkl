# Generated by Django 3.0 on 2020-03-16 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_auto_20200316_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patent',
            name='app_year',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='patent',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
