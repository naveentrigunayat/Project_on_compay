from django.db import models
from django.contrib.auth.models import User

class Income(models.Model):
    income=models.IntegerField()
    incomeType=models.CharField(max_length=30)
    incomeDate=models.DateField() #auto_now=True
    description=models.TextField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

from django import forms

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields=['income','incomeType','incomeDate','description']