from rest_framework import viewsets
from .models import Sector, Skill, Profile, Company, Job, Location
from django.contrib.auth.models import User, Group
from .serializers import SectorSerializer, SkillSerializer, LocationSerializer, CompanySerializer, JobSerializer, UserSerializer, GroupSerializer, ProfileSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
# Create your views here.
class SectorViewSets(viewsets.ModelViewSet):
    queryset = Sector.objects.all()
    serializer_class = SectorSerializer


class SkillViewSets(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer    


class LocationViewSets(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class CompanyViewSets(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class JobViewSets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class UserViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer