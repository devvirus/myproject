from django.contrib.auth.models import User,Group
from myapp.models import Student,Publisher,Author,Book 
from userapp.models import RegistrationData 
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=User
		fields=['url', 'username', 'email', 'groups']
		
class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Group
		fields = ['url', 'name']

class StudentSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Student
		fields=['sname','smobile']
class PublisherSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Publisher
		fields=['publisher_name','publisher_email']		
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Author
		fields=['auther_name','auth_email']
class BookSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Book
		fields=['bname','bcost']
class RegistrationDataSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=RegistrationData
		fields=['first_name','last_name','mobile','email','username']		