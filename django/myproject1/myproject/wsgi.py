"""
WSGI config for myproject project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

sys.path.append('/home/portal/python/django/myproject') 
# adjust the Python version in the line below as needed 
sys.path.append('/usr/lib/python2.7/site-packages') 



application = get_wsgi_application()
