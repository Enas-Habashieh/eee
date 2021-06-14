"""myfirsttest URL Configuration

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

from my_first_testapp import views, viewsemployee

urlpatterns = [
    ##department
    path('postdepartment',views.adddepartmentview),
    path('deletedepartment/<int:pk>',views.deletedepartmentview),
    path('updatedepartment/<int:pk>', views.updatedepartmentview),
    path('getbyiddepartment/<int:pk>',views.getbyiddepartmentview),
    path('getalldepartment',views.getalldepartmentview),
    ##employee
    path('postemployee',viewsemployee.addemployeeview),
    path('deleteemployee/<int:pk>',viewsemployee.deleteemployeeview),
    path('updateemployee/<int:pk>',viewsemployee.updateemployeeview),
    path('getbyidemployee/<int:pk>',viewsemployee.getbyidemployeeyview),
    path('getallemployee',viewsemployee.getllemployeeview),
    path('getparam', viewsemployee.getemployeeparamview),
]
