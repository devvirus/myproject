# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import RegistrationData

# Register your models here.

class AdminRegistrationData(admin.ModelAdmin):
	list_display=['first_name','last_name','mobile','email','username','password','confirm_password']
admin.site.register(RegistrationData,AdminRegistrationData)		


