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
from app01 import views


urlpatterns = [
    ##url(r'^admin/', admin.site.urls),
    url(r'modal_edit_class',views.modal_edit_class),
    url(r'login/', views.login),
    url(r'index',views.index),
    url(r'modal_new_student/', views.modal_new_student),
    url(r'edit_student/',views.edit_student),
    url(r'classes/',views.classes),
    url(r'new_student/', views.new_student),
    url(r'new',views.new),
    url(r'del_class',views.del_class),
    url(r'edit_class/',views.edit_class),
    url(r'student/',views.student),

    url(r'modal_add_class',views.modal_add_class),





]
