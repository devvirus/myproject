# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class RegistrationData(models.Model):
	first_name=models.CharField(max_length=50)
	last_name=models.CharField(max_length=50)
	mobile=models.BigIntegerField()
	email=models.EmailField(max_length=50)
	username=models.CharField(max_length=50)
	password=models.CharField(max_length=100)
	confirm_password=models.CharField(max_length=100)





# Create your models here.
