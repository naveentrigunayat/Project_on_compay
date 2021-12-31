from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    expense=models.IntegerField()
    expenseType=models.CharField(max_length=30)
    expenseDate=models.DateField() #auto_now=True
    description=models.TextField(max_length=300)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

from django import forms
class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields='__all__'