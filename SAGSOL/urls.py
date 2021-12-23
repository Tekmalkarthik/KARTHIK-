"""SAGSOL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',views.home),
    path("formlink1",views.formlink1),
    path('',views.mylogin,name='login'),
    path('login',views.mylogin,name='login'),
    path('insertdata',views.insertdata),
    path('signin',views.signin),
    path('formlink',views.formlink),
    path("userdata",views.userdata),









    
    path("Form_2",views.Form_2),
    path("Form_3",views.Form_3),
    path("Form_4",views.Form_4),
    path("Form_5",views.Form_5),
    path("Form_6",views.Form_6),
    path("Form_7",views.Form_7),
    path("Form_8",views.Form_8),
    path("Form_9",views.Form_9),
    path("Form_10",views.Form_10),
    path("Form_11",views.Form_11),
    path("Form_12",views.Form_12),
    #path('save',views.save_data),
    path("kar",views.kar)

]
