# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Publisher,Author,Student,Book

class AdminPublisher(admin.ModelAdmin):
	list_display=['publisher_name','publisher_email']
class AdminAuthor(admin.ModelAdmin):
	list_display=['auther_name','auth_email']	
class AdminStudent(admin.ModelAdmin):
	list_display=['sname','smobile']
class AdminBook(admin.ModelAdmin):
	list_display=['bname','bcost']
admin.site.register(Publisher,AdminPublisher)	
admin.site.register(Author,AdminAuthor)	
admin.site.register(Student,AdminStudent)	
admin.site.register(Book,AdminBook)	

# Register your models here.
