"""pythonWepProgramming URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path # 한글 슬러그를 위해 re_path()사용
from bookmark.views import BookmarkLV, BookmarkDV

app_name = 'bookmark'
urlpatterns = [
    
    path('bookmark/', BookmarkLV.as_view(), name = 'index'),
    path('bookmark/<int:pk>/', BookmarkDV.as_view(), name = 'detail'),
    
]
