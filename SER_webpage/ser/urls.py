"""SRE_webpage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path,include
from . import views
from . import upl
import os

from django.urls import path
from . import views

urlpatterns = [
    
]
urlpatterns = [
    
    path('',views.login, name= 'login'),
    path('up/',views.to_upload, name= 'to_upload'),
    path('re/',views.to_rec, name= 'to_rec'),
    
    path('u/',views.abs, name= 'abs'),
    path('r/',views.rec1, name= 'rec1'),
    path('r1/',views.sb, name= 'sb'),
   

]
