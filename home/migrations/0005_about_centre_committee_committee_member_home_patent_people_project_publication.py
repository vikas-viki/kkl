# Generated by Django 3.0 on 2020-01-23 19:25

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_conference_students'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_us', models.CharField(max_length=3000)),
                ('image1', models.ImageField(blank=True, upload_to='home/static/home/images/about_us')),
                ('image2', models.ImageField(blank=True, upload_to='home/static/home/images/about_us')),
            ],
        ),
        migrations.CreateModel(
            name='centre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('youtube_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='committee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('scope', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('director_message', models.CharField(max_length=3000)),
                ('director_image', models.ImageField(blank=True, upload_to='home/static/home/images/home')),
                ('annual_report', models.FileField(blank=True, upload_to='home/static/home/files/home')),
                ('one_liner', models.CharField(max_length=50)),
                ('happening1', models.CharField(max_length=1000)),
                ('happening2', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='patent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('app_year', models.IntegerField()),
                ('status', models.CharField(choices=[('1', 'Completed'), ('2', 'Running'), ('3', 'To be started')], max_length=1)),
                ('type', models.CharField(max_length=30)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('category', models.CharField(choices=[('1', 'PhD'), ('2', 'Alumni'), ('3', 'Research Investigator'), ('4', 'Other Member')], max_length=1)),
                ('designation', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, upload_to='home/static/home/images/people')),
                ('research_interests', models.CharField(max_length=500)),
                ('bio', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('status', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('funding_agency', models.CharField(max_length=300)),
                ('amount', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='publication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=40)),
                ('yop', models.DateField()),
                ('journal', models.CharField(max_length=40)),
                ('link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='committee_member',
            fields=[
                ('committee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='home.committee')),
                ('name', models.CharField(max_length=40)),
                ('designation', models.CharField(max_length=40)),
            ],
        ),
    ]
