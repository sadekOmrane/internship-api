from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Sector(models.Model):
    title = models.CharField(max_length=48)


    def __str__(self):
        return self.title
    

class Skill(models.Model):
    title = models.CharField(max_length=48)
    sectors = models.ManyToManyField(Sector)

    def __str__(self):
        return self.title


class Profile(models.Model):
    title = models.CharField(max_length=48)
    resume = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    skills = models.ManyToManyField(Skill)


    def __str__(self):
        return self.title

class Location(models.Model):
    country = models.CharField(max_length=48)
    city = models.CharField(max_length=48)
    zipcode = models.IntegerField()
    address = models.CharField(max_length=255)

    
    def __str__(self):
        return self.address + ', ' + self.zipcode.__str__() + ', ' + self.city + ', ' + self.country


class Company(models.Model):
    name = models.CharField(max_length=48)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    sectors = models.ManyToManyField(Sector, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)


    def __str__(self):
        return self.name

class Job(models.Model):
    title = models.CharField(max_length=48)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    skills = models.ManyToManyField(Skill)
    candidates = models.ManyToManyField(User)  
    status = models.BooleanField(default=True)  


    def __str__(self):
        return self.title

