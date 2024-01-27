# Generated by Django 3.0 on 2020-03-14 21:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_auto_20200213_2344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='brief',
        ),
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='writer',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='news',
            name='headline',
            field=models.CharField(max_length=500),
        ),
    ]