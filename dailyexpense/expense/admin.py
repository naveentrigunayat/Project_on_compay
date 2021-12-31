from django.contrib import admin

from expense.models import Expense

class ExpenseAdmin(admin.ModelAdmin):
    list_display=['id','expense','expenseType','expenseDate','description','user']
    list_filter=['expense','expenseDate','user']
admin.site.register(Expense,ExpenseAdmin)
