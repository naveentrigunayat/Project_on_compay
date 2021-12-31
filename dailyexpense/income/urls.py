
from django.contrib import admin
from django.urls import path
from .import views as v
urlpatterns = [
    path('income', v.add_income,name="addincome"),
    path('-incomelist', v.income_list,name="incl"),
    path('delete_income/<int:id>',v.income_delete,name="income_delete"),
]
