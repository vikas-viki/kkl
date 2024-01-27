# Generated by Django 3.0 on 2020-03-29 22:26

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_auto_20200316_1535'),
    ]

    operations = [
        migrations.DeleteModel(
            name='conference',
        ),
        migrations.AlterField(
            model_name='patent',
            name='status',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='people',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, unique=True),
        ),
    ]