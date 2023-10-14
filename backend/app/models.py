from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sector(models.Model):
    title = models.CharField(max_length=48)


class Skill(models.Model):
    title = models.CharField(max_length=48)
    sector = models.ManyToManyField(Sector)


class Profile(models.Model):
    title = models.CharField(max_length=48)
    resume = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)


class Location(models.Model):
    country = models.CharField(max_length=48)
    city = models.CharField(max_length=48)
    zipcode = models.IntegerField()
    address = models.CharField(max_length=255)


class Company(models.Model):
    name = models.CharField(max_length=48)
    description = models.TextField()
    location = models.CharField(max_length=48)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    sectors = models.ManyToManyField(Sector)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)


class Job(models.Model):
    title = models.CharField(max_length=48)
    description = models.CharField(max_length=48)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    skills = models.ManyToManyField(Skill)
    candidates = models.ManyToManyField(User)  
    status = models.BooleanField(default=True)  

