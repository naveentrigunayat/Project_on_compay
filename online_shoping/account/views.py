from django.shortcuts import render,redirect,HttpResponse
from product.models import Category,Product
from .models import User,UserForm,UserInfo,LoginForm
from django.contrib.auth import login,logout,authenticate

def home(request):
    cl=Category.objects.all()
    pl=Product.objects.all()
    d={'cl':cl,'pl':pl}
    return render(request,'home.html',d)


def register(request):
    cl=Category.objects.all()
    pl=Product.objects.all()

    if request.method=='POST':
        f=UserForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f=UserForm
        d={'pl':pl,'cl':cl,'form':f}
        return render(request,'form.html',d)

def login_view(request):
    cl=Category.objects.all()
    pl=Product.objects.all()

    if request.method=='POST':
        uname=request.POST.get('UserName')
        passw=request.POST.get('Password')
        user=authenticate(request,username=uname,password=passw)
        if user is not None:
            request.session['uid']=user.id
            login(request,user) 
            return redirect('/')
        else:
            return HttpResponse('<h1>InValid UserName and Password</h1>')
    else:
        f=LoginForm
        d={'pl':pl,'cl':cl,'form':f}
        return render(request,'form.html',d)

def logout_view(request):
    logout(request)
    return redirect('/')