from rest_framework import serializers
from .models import Sector, Skill, Profile, Company, Job, Location
from django.contrib.auth.models import User, Group


# Create your serializers here.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SectorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sector 
        fields = ('id', 'title')


class SkillSerializer(serializers.HyperlinkedModelSerializer):
    sector = SectorSerializer(read_only=True)
    class Meta:
        model = Skill 
        fields = ('id', 'title', 'sector')


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location 
        fields = ('id', 'country', 'city', 'zipcode', 'address')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    skills = SkillSerializer(read_only=True)
    class Meta:
        model = Profile 
        fields = ('id', 'title', 'user', 'skills')


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    owner = UserSerializer(read_only=True)
    sectors = SectorSerializer(read_only=True)
    location = LocationSerializer(read_only=True)
    class Meta:
        model = Company 
        fields = ('id', 'name', 'description', 'owner', 'sectors', 'location')


class JobSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(read_only=True)
    candidates = UserSerializer(read_only=True)
    skills = SkillSerializer(read_only=True)
    class Meta:
        model = Job 
        fields = ('id', 'title', 'description', 'company', 'candidates', 'skills', 'status')



