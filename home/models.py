from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

status_choices = [
    ('1','Completed'),
    ('2','Running'),
    ('3','To be started'),
]

people_category_choices = [
    ('1','PhD'),
    ('2','Alumni'),
    ('3','Research Investigator'),
    ('4','Other Member'),
]

class home(models.Model):
    director_message = models.CharField(max_length=5000)
    director_image = models.ImageField(upload_to='home/static/home/images/home',blank=True)
    annual_report = models.FileField(upload_to='home/static/home/files/home',blank=True)
    one_liner = models.CharField(max_length=50)
    happening1 = models.CharField(max_length=1000)
    happening2 = models.CharField(max_length=1000)

class about(models.Model):
    about_us = models.CharField(max_length=5000)
    image1 = models.ImageField(upload_to='home/static/home/images/about_us',blank=True)
    image2 = models.ImageField(upload_to='home/static/home/images/about_us',blank=True)

class centre(models.Model):
    centre_name = models.CharField(max_length=30)
    content_topic = models.CharField(max_length=150,null=True)
    content = models.CharField(max_length=2000,null=True)
    image = models.ImageField(upload_to='home/static/home/images/centres',blank=True)
    youtube_link = models.URLField(blank=True)

#class project needs to be linked with class peoploe
class project(models.Model):
    status = models.CharField(max_length=100)
    pi = models.CharField(max_length=100,null=True)
    copi = models.CharField(max_length=100,blank=True)
    title  = models.CharField(max_length=300,primary_key=True)
    funding_agency = models.CharField(max_length=300)
    amount = models.CharField(max_length=100,null=True)
    duration = models.CharField(max_length=100,null=True)

class publication(models.Model):
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=400)
    yop = models.CharField(max_length=10)
    journal = models.CharField(max_length=100)
    link = models.URLField(blank=True)

    def __str__ (self):
        return self.title

class patent(models.Model):
    title = models.CharField(max_length=300)
    app_year = models.CharField(max_length=10)
    status = models.CharField(max_length=20)
    type = models.CharField(max_length=30)
    link = models.URLField(blank=True)

class people(models.Model):
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30,blank=True,null=True)
    last_name = models.CharField(max_length=30)
    category = models.CharField(max_length=1,choices=people_category_choices)
    designation = models.CharField(max_length=150)
    image = models.ImageField(upload_to='kavikrishna_lab/static/home/images/people',blank=True)
    research_interests = models.CharField(max_length=500)
    bio = models.CharField(max_length=300,null=True, blank=True)
    email = models.EmailField()
    phone = PhoneNumberField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class collaborator(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    brief = models.CharField(max_length=1000)
    link = models.URLField(blank=True)
    def __str__(self):
        return self.name + ' - ' + str(self.date)

#model committee linked with committee_members
class committee(models.Model):
    name = models.CharField(max_length=50)
    scope = models.CharField(max_length=2000)

class committee_member(models.Model):
    committee = models.OneToOneField(committee,on_delete = models.CASCADE, primary_key = True)
    name = models.CharField(max_length=40)
    designation = models.CharField(max_length=40)

class academic(models.Model):
    name = models.CharField(max_length=40)
    brief1 = models.CharField(max_length=40)
    brief2 = models.CharField(max_length=40)

class facility(models.Model):
    instrument_name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='home/static/home/images/facilities',blank=True)
    function = models.CharField(max_length=1500)
    remarks = models.CharField(max_length=1000)

class news(models.Model):
    headline = models.CharField(max_length=500)
    writer = models.CharField(max_length=100)
    link = models.URLField(blank=True)
    image = models.ImageField(upload_to='home/static/home/images/news')
    date = models.DateField(null=True)
