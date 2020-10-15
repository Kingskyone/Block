"""Block URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from app import views

urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('login/', views.loginpage, name="loginpage"),
    path('sign/', views.signpage, name="signpage"),
    path('loginS/', views.loginS, name="loginS"),
    path('signS/', views.signS, name="signS"),
    path('submitS/', views.submitS, name="submitS"),
    path('talkS/', views.talkS, name="talkS"),
    path('logout/', views.logout, name="logout"),
    path('inf/', views.infpage, name="inf"),
    path('submit/', views.submitpage, name="submit"),
    path('changepwd/', views.changepwd, name="changepwd"),
    path('changepwdS/', views.changepwdS, name="changepwdS"),
    path('returnpwd/', views.returnpwd, name="returnpwd"),
    path('returnpwdS/', views.returnpwdS, name="returnpwdS"),
    path('admin/', views.admin, name="admin"),
    path('admin_message_show/', views.admin_message_show, name="admin_message_show"),
    path('delete_message/', views.delete_message),
    path('admin_talk_show/', views.admin_talk_show, name="admin_talk_show"),
    path('delete_talk/', views.delete_talk),
    path('admin_user_show/', views.admin_user_show, name="admin_user_show"),
    path('delete_user/', views.delete_user),
    path('change_aut/', views.change_aut),
    re_path('detail/(?P<bk_id>[0-9]+)', views.detailpage, name="detailpage"),
    #re_path('rank1/(?P<num>[012])', views.rank1, name="rank1"),
]
