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
    sectors = SectorSerializer(many=True, read_only=True)
    sector_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True,queryset=Sector.objects.all())
    class Meta:
        model = Skill 
        fields = ('id', 'title', 'sectors', 'sector_ids')
        
    def create(self, validated_data):
        sectors_data = validated_data.pop('sector_ids')
        skill = Skill.objects.create(**validated_data)
        skill.sectors.set(sectors_data)
        return skill
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        if('sector_ids' in validated_data):
            sectors_data = validated_data.pop('sector_ids')
            sectors = instance.sectors
            sectors.set(sectors_data)
        return instance


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location 
        fields = ('id', 'country', 'city', 'zipcode', 'address')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())
    skills = SkillSerializer(many=True, read_only=True)
    skill_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True, queryset=Skill.objects.all())
    class Meta:
        model = Profile 
        fields = ('id', 'title', 'user', 'user_id', 'skills', 'skill_ids')
    
    def create(self, validated_data):
        skills_data = validated_data.pop('skill_ids')
        user_data = validated_data.pop('user_id')
        profile = Profile.objects.create(user = user_data, **validated_data)
        profile.skills.set(skills_data)
        return profile

    def update(self, instance, validated_data):
        if'user_id' in validated_data:
            user_data = validated_data.pop('user_id')
            user = instance.user
            user.set(user_data)
        instance.user = validated_data.get('user_id', instance.user)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        if('skill_ids' in validated_data):
            skills_data = validated_data.pop('skill_ids')
            skills = instance.skills
            skills.set(skills_data)
        return instance

class CompanySerializer(serializers.HyperlinkedModelSerializer):
    owner = UserSerializer(read_only=True)
    owner_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=User.objects.all())
    sectors = SectorSerializer(many=True, read_only=True)
    sector_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True,queryset=Sector.objects.all())
    location = LocationSerializer(read_only=True)
    location_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Location.objects.all())
    class Meta:
        model = Company 
        fields = ('id', 'name', 'description', 'owner', 'owner_id', 'sectors', 'sector_ids', 'location', 'location_id')
    
    def create(self, validated_data):
        sectors_data = validated_data.pop('sector_ids')
        owner_data = validated_data.pop('owner_id')
        location_data = validated_data.pop('location_id')
        company = Company.objects.create(owner = owner_data, location = location_data, **validated_data)
        company.sectors.set(sectors_data)
        return company
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('name', instance.description)
        instance.owner = validated_data.get('owner_id', instance.owner)
        instance.location = validated_data.get('location_id', instance.location)
        instance.sectors.set(validated_data.get('sector_ids', instance.sectors))
        instance.save()
        return instance


class JobSerializer(serializers.HyperlinkedModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.PrimaryKeyRelatedField(write_only=True,queryset=Company.objects.all())
    candidates = UserSerializer(read_only=True, many=True)
    candidate_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True,queryset=User.objects.all())
    skills = SkillSerializer(read_only=True, many=True)
    skill_ids = serializers.PrimaryKeyRelatedField(many=True, write_only=True,queryset=Skill.objects.all())
    class Meta:
        model = Job 
        fields = ('id', 'title', 'description', 'company', 'company_id', 'candidates', 'candidate_ids', 'skills', 'skill_ids', 'status')
    

    def create(self, validated_data):
        company_data = validated_data.pop('company_id')
        candidates_data = validated_data.pop('candidate_ids')
        skills_data = validated_data.pop('skill_ids')
        job = Job.objects.create(company = company_data, **validated_data)
        job.candidates.set(candidates_data)
        job.skills.set(skills_data)
        return job
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.status = validated_data.get('status', instance.status)
        instance.candidates.set(validated_data.get('candidate_ids', instance.candidates))
        instance.company = validated_data.get('company_id', instance.company)
        instance.skills.set(validated_data.get('skill_ids', instance.skills))
        instance.save()
        return instance


