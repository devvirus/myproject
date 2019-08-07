# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Publisher,Author,Student,Book


def home(request):
	student_data=Student.objects.all()
	publisher_data=Publisher.objects.all()
	auther_data=Author.objects.all()
	book_data=Book.objects.all()
	return render(request,'staticfiles.html',{'student_data':student_data,'publisher_data':publisher_data,'auther_data':auther_data,'book_data':book_data})

# Create your views here.
