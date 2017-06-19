"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
import os.path as op
import sys

APP_DIR =  op.join(op.dirname(op.abspath(__file__)))
PRJ_DIR = op.dirname(APP_DIR)
sys.path.insert(0, PRJ_DIR)
from qa.views import test

urlpatterns = [
    #url(r'^admin/', admin.site.urls),
    url(r'^$', test),
    url(r'^login/$', test),
    url(r'^signup/$', test),
    url(r'question/\d+/$', test),
    url(r'^ask/$', test),
    url(r'^popular/$', test),
    url(r'^new/$', test)
]