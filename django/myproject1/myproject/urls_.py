"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include,url
#from django.urls import include,path
from django.contrib import admin
from rest_framework import routers
from quickstart import views as appview
from myapp import views as myapp_view
from userapp import views as user_view

router=routers.DefaultRouter()
router.register(r'users', appview.UserViewSet)
router.register(r'groups', appview.GroupViewSet)
router.register(r'student', appview.StudentViewSet)
router.register(r'publisher', appview.PublisherViewSet)
router.register(r'book', appview.BookViewSet)
router.register(r'author', appview.AuthorViewSet)
router.register(r'registeruser', appview.RegistrationDataViewSet)
router.register(r'demoview', appview.RegisterView)
urlpatterns = [
    url('', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^login/',user_view.login_view),
	url(r'^register/',user_view.registration_view),
	url(r'^home/',user_view.home_view),
	url(r'^logout/',user_view.logout_view,name='logout'),
	url(r'^admin/', admin.site.urls),
	#url(r'hello/', appview.HelloView.as_view(), name='hello'),
	#url(r'demoview/', appview.RegisterView.as_view(), name='registerview'),
]
'''urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^login/',views.login_view),
	url(r'^register/',views.registration_view),
	url(r'^home/',views.home_view),
	url(r'^logout/',views.logout_view,name='logout')
	
]'''
