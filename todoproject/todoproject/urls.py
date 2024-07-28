"""
URL configuration for todoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from todoapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('reg', views.Userregistrationview.as_view(),name='reg_view'),
    path('log',views.UserLoginview.as_view(),name='login_view' ),
    path('home',views.Home.as_view(),name='home_view'),
    path('out',views.Logoutview.as_view(),name="logout_view"),
    path('create',views.TodoCreateview.as_view(),name="create_view"),
    path('list',views.TodoListView.as_view(),name="list_view"),
    path('edit/<int:id>',views.TodoEditView.as_view(),name="edit_view"),
    path('delete//<int:id>',views.TodoDeleteView.as_view(),name="delete_view"),
    path('',views.Home.as_view(),name='user_home'),
    path('user/home',views.UserHomeView.as_view(),name='userhome_view'),
    path('user/profile',views.UserProfileView.as_view(),name='userprofile_view'),
  
]
