# Generated by Django 3.0 on 2020-01-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_conference'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='students',
            field=models.IntegerField(null=True),
        ),
    ]
