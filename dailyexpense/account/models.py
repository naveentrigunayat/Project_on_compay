from django.db import models

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

from django import forms

class UserInfo(User):
    age=models.IntegerField()
    gender=models.CharField(max_length=30)
    contact=models.CharField(max_length=15)
    class Meta:
        db_table="userinfo"

class UserForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['username','first_name','last_name',"age","contact","gender",'email','password1','password2']
