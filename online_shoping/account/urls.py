
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('register', v.register,name='register'),
    path('login', v.login_view,name='login'),
    path('logout', v.logout_view,name='logout'),
]
