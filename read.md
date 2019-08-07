On deploy cammand 

python manage.py collectstatic

################################# Python Project ##########################
<VirtualHost *:80>
ServerName python.uat.webcnk.com
DocumentRoot /home/portal/python/django/myproject1/
#Alias /media/ /path/to/mysite.com/media/
#Alias /static/ /home/portal/python/django/myproject1/static/

<Directory /home/portal/python/django/myproject1>
Require all granted
</Directory>
WSGIDaemonProcess python.uat.webcnk.com python-path=/home/portal/python/django/myproject1/
WSGIScriptAlias / /home/portal/python/django/myproject1/myproject/wsgi.py
</VirtualHost>
####################################################################


system.py


#################################################
#on diploy
STATIC_ROOT="/home/portal/python/django/myproject1/static/";
STATIC_URL = '/static/'
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(__file__), 'templates'),
)
STATICFILES_DIR=[
                os.path.join(BASE_DIR, "static")
]
###################################

URLS.py

from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [ ……
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
