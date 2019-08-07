# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.conf import settings
from .forms import RegistrationForm,LoginForm
from .models import RegistrationData
from django.http.response import HttpResponse
from django.views.decorators.cache import cache_page 
from django.core.cache import cache

# Create your views here.
@cache_page(60*1)
def registration_view(request):
	if request.method=='POST':
		rform=RegistrationForm(request.POST)
		if rform.is_valid():
			first_name=request.POST.get('first_name','')
			last_name=request.POST.get('last_name','')
			mobile=request.POST.get('mobile','')
			email=request.POST.get('email','')
			username=request.POST.get('username','')
			password=request.POST.get('password','')
			confirm_password=request.POST.get('confirm_password','')
			data=RegistrationData(
				first_name=first_name,
				last_name=last_name,
				mobile=mobile,
				email=email,
				username=username,
				password=password,
				confirm_password=confirm_password,
			)
			data.save()
			lform=LoginForm()
			return render(request,'login.html',{'lform':lform})
	else:
		rform=RegistrationForm()
		return render(request,'registration.html',{'rform':rform})

@cache_page(60*1)		
def login_view(request):
	if request.method=='POST':
		lform=LoginForm(request.POST)
		if lform.is_valid():
			uname=request.POST.get('username','')
			pwd=request.POST.get('password','')
			uservalid=RegistrationData.objects.filter(username=uname,password=pwd)
			res=''
			if uservalid:
				for user in uservalid:
					res=user.username
				request.session['username'] = res
				return redirect('/home/')
			else:
				return HttpResponse('InValid User')
	else:
		lform=LoginForm()
		return render(request,'login.html',{'lform':lform})


def home_view(request):
	if 'username' in request.session:
		x=request.session['username']
		RegistratioData=RegistrationData.objects.filter(username=x)
		#tmpJson = serializers.serialize("json",RegistratioData)
		#tmpObj = json.loads(tmpJson)
		#return HttpResponse(x)
		return render(request,'home.html',{'RegistratioData':RegistratioData})
	else:
		return redirect('/login/')

def logout_view(request):
	try:
		del request.session['username']
	except:
		pass
	return redirect('/login')	

	
		
		
			
		
		
		
			
			
			