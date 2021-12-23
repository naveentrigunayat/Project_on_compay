from django.forms import ModelForm

from django import forms

from .models import Employee
from .models import Department
from .models import Designation

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = "__all__"
