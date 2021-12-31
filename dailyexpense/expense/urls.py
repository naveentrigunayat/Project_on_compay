
from django.contrib import admin
from django.urls import path
from . import views as v
urlpatterns = [
    path('expense',v.add_expense,name='addexpense'),
    path('-expenselist',v.expense_list,name='expl'),
]
