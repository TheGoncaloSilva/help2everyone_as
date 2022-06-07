from distutils.command.upload import upload
import datetime
from email.policy import default
from django.db import models
from django.forms import IntegerField

# Create your models here.
# For the tables to appear in admin, dont forget to alter in admin.py app file
class Voluntary(models.Model):
    profileImg = models.ImageField(upload_to = 'voluntary_images', default = 'blank-profile-picture.png')
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField()
    registryDate = models.DateField(default=datetime.date.today)
    phoneNumber = models.IntegerField(default=0)
    ageOfBirth = models.DateField(default=datetime.date.today)
    password = models.CharField(max_length=300)


class Organization(models.Model):
    #Organization_id = models.models.AutoField(_(""))
    orgImg = models.ImageField(upload_to = 'organization_images', default = 'blank-profile-picture.png')
    orgName = models.CharField(max_length=100)
    email = models.EmailField()
    contactNumber = models.IntegerField(default=0)
    websiteAddress = models.CharField(max_length=250)
    foundationDate = models.DateField(default=datetime.date.today)
    registryDate = models.DateField(default=datetime.date.today)
    password = models.TextField(max_length=300)


class Event(models.Model):
    eventMainImage = models.ImageField(upload_to = 'events_images', default = 'event-default.png')
    eventName = models.CharField(max_length=100)
    shortDescription = models.CharField(max_length=90)
    description = models.CharField(max_length=1000)
    totalVoluntarys = models.IntegerField(default=1)
    address = models.CharField(max_length=200)
    zipCode = models.CharField(max_length=8)
    district = models.CharField(max_length=100) # distrito  
    county = models.CharField(max_length=100) # concelho
    parish = models.CharField(max_length=100) # freguesia
    startDate = models.DateField(default=datetime.date.today)
    endDate = models.DateField(default=datetime.date.today)
    idOrganization = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Voluntary_Events(models.Model):
    voluntaryId = models.ForeignKey(Voluntary, on_delete=models.CASCADE)
    organizationId = models.ForeignKey(Organization, on_delete=models.CASCADE)
