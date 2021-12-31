from django.shortcuts import render,redirect
from account.views import getbalance
from .models import Expense,ExpenseForm


def add_expense(request):

    if request.method=='POST':
        f=ExpenseForm(request.POST)
        #if getbalance(request)>
        f.save()
        return redirect('/')
    else:
        f=ExpenseForm
        d={'form':f}
        return render(request,'form.html',d)

def expense_list(request):
    userid=request.session.get("userid")
    expl=Expense.objects.filter(user=userid)
    return render(request,'expenselist.html',{'exp':expl})