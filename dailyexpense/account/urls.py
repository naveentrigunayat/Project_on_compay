
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('register',v.add_user,name="adduser"), 
    path('-login',v.login_view,name="login"), 
    path('-logout',v.logout_view,name="logout"), 
    path('-update-profile',v.edit_profile,name="editprofile"), 
]

# appname mappingName
# url
