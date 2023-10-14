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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    skills = models.ManyToManyField(Skill)


class Company(models.Model):
    firstName = models.CharField(max_length=48)
    lastName = models.CharField(max_length=48)
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    sector = models.ManyToManyField(Sector)


class Job(models.Model):
    title = models.CharField(max_length=48)
    description = models.CharField(max_length=48)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="jobs")
    skills = models.ManyToManyField(Skill)
    candidates = models.ManyToManyField(User)    
