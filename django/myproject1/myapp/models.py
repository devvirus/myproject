# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Publisher(models.Model):
	publisher_name=models.CharField(max_length=500)
	publisher_email=models.EmailField(max_length=50)
	
	def __str__(self):
		return self.publisher_name

class Author(models.Model):
	abc=models.OneToOneField(Publisher,on_delete=models.CASCADE,null=True)
	auther_name=models.CharField(max_length=500)
	auth_email=models.EmailField(max_length=50)
	def __str__(self):
		return self.auther_name

class Student(models.Model):
	sname=models.CharField(max_length=50)
	smobile=models.IntegerField()
	
	def __str__(self):
		return self.sname
class Book(models.Model):
	bname=models.CharField(max_length=50)
	bcost=models.IntegerField()
	
	def __str__(self):
		return self.bname
		
	
	

# Create your models here.
