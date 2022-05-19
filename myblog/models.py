from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

# Create your models here.
# create automatically tables or DB with classes
class Post(models.Model):

    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + '|' + str(self.author)

    def get_absolute_url(self):
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')

'''class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=120)
    address = models.CharField(max_length=300)
    zip_code = models.CharField('Zip Code', max_length=15)
    phone = models.CharField('Contact Phone',max_length=25)
    web = models.URLField('website Address')
    email_address = models.EmailField('Email Address')

    def __str__(self):
        return self.name

class MyClubUser(models.Model):

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Event(models.Model):#table DB
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event Date')
    #connect two differents tables Venue and this(one to one)
    venue = models.ForeignKey(Venue, blank=True,null=True,on_delete=models.CASCADE)
    #venue = models.CharField(max_length=120)
    manager = models.CharField(max_length=60)
    description = models.TextField(blank=TRUE)
    #link to many people to many events(many table to many table)
    attendees = models.ManyToManyField(MyClubUser, blank=True)
    
    def __str__(self):
        return self.name'''

        