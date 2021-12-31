"""newsapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from news import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = "home"),
    path('add1/', views.add1, name="add1"),
    path('add2/', views.add2, name="add2"),
    path('add3/', views.add3, name="add3"),
    path('add4/', views.add4, name="add4"),
    path('add5/', views.add5, name="add5"),
    path('add6/', views.add6, name="add6"),
    path('add7/', views.add7, name="add7"),
    path('add8/', views.add8, name="add8"),
]
