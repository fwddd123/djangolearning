"""mysite URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
import requests

from django.shortcuts import HttpResponse,render,redirect
def login(request):
    #return HttpResponse('login.html')
    #print(request.method)
    if request.method=='GET':

        return render(request,'login.html')
    else:
        u= request.POST.get('user')
        p= request.POST.get('pwd')
        print(u,p)
        if u=='root' and p=='123456':
            return redirect('/index/')
        else:
            return render(request,'login.html',{'msg':'123456'})
def index(request):
    return render(
        request,'index.html',
        {
            'name':'alex',
            'users':['123','123'],
            'user_dict':{'k1':'v1','k2':'v2'},
        }
    )
urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    url(r'login/', login),
    url(r'index',index),
]
