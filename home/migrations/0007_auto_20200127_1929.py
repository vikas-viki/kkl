# Generated by Django 3.0 on 2020-01-27 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200124_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='middle_name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
