from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Income,IncomeForm

def add_income(request):

    if request.method=='POST':
        f=IncomeForm(request.POST)
        #userid=request.session.get("userid")
        #us=User.objects.get(id=userid)
        #f.user=us
        f.save()
        return redirect('/')
    else:
        f=IncomeForm
        d={'form':f}
        return render(request,'form.html',d)

def income_list(request):
    userid=request.session.get("userid")
    incl=Income.objects.filter(user=userid)
    inc=set()
    dl=set()
    inct=set()
    for i in incl:
        inc.add(i.income)
    
    for i in incl:
        dl.add(i.incomeType)
    
    for i in incl:
        inct.add(i.incomeDate)
        

    d={'inc':incl,"income":inc,"inct":inct,"dl":dl}
    return render(request,'incomelist.html',d)

def income_delete(request,id):
    income=Income.objects.get(id=id)
    income.delete()
    return redirect('/')