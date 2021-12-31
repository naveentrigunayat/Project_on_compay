from django.shortcuts import render,redirect,HttpResponse
from .models import User,UserInfo,UserForm
from expense.models import Expense
from income.models import Income

def getbalance(request):
    uid=request.session.get("userid")
    incl=Income.objects.filter(user=uid)
    expl=Expense.objects.filter(user=uid)
    totalIncome=0
    totalExpense=0

    for i in incl:
        totalIncome=totalIncome+i.income
    
    for i in expl:
        totalExpense=totalExpense+i.expense
    return totalIncome-totalExpense


def home(request):
    for i in request.session.items():
        print(" ---------- ",i)
    return render(request,'home.html',{'bal':getbalance(request)})

def add_user(request):

    if request.method=='POST': 
        f=UserForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserForm
        d={'form':f}
        return render(request,'form.html',d) 

from django.contrib.auth import authenticate,login,logout
def login_view(request):

    if request.method=='POST': 
        uname=request.POST.get('uname')
        passw=request.POST.get('passw')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['userid']=user.id
            login(request,user)
            return redirect('/')
        else:
            return HttpResponse("InValid UserName ANd Password")
    else:
        return render(request,'login.html') 


def logout_view(request):
    logout(request)
    return redirect('/')

def edit_profile(request):
    uid=request.session.get("userid")
    us=UserInfo.objects.get(id=uid)
    if request.method=='POST':
        f=UserForm(request.POST,instance=us)
        f.save()
        return redirect('/')
    else:    
        f=UserForm(instance=us)
        return render(request,'form.html',{'form':f})