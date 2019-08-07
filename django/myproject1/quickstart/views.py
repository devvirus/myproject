# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User,Group
from myapp.models import Student,Publisher,Author,Student,Book 
from userapp.models import RegistrationData 
from rest_framework import viewsets
#from rest_framework.views import APIView
from rest_framework.response  import Response
from rest_framework.permissions  import IsAuthenticated  
from quickstart.serializers import UserSerializer, GroupSerializer,StudentSerializer,PublisherSerializer,AuthorSerializer,BookSerializer,RegistrationDataSerializer 
from django.core import serializers
from django.http import HttpResponse
import json


class UserViewSet(viewsets.ModelViewSet):

	queryset=User.objects.all().order_by('-date_joined')
	serializer_class=UserSerializer
	
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer	
	
class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer	
class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer	

class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer		
class BookViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer		

class RegistrationDataViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
	
    queryset = RegistrationData.objects.all()
    serializer_class = RegistrationDataSerializer	
	

class RegisterView(viewsets.ModelViewSet):
	
	permission_classes = (IsAuthenticated,)
	queryset = RegistrationData.objects.all()
	serializer_class = RegistrationDataSerializer
		
		
		
		
	
	
# Create your views here.
