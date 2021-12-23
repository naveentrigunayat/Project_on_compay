from django.shortcuts import render
from .models import Employee
from .form import EmployeeForm

# Create your views here.
def Welcome(request):
    return render(request,"welcome.html")


def load_form(request):
    form = EmployeeForm
    return render(request,'index.html',{'form ' : form})



def add(request):
    form = EmployeeForm(request.POST)
    form.save()
    





