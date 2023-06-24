from django import forms
from .models import *

class departmentForm(forms.ModelForm):
    
    class Meta:
        model = department
        fields = "__all__"

class employeeForm(forms.ModelForm):
    
    class Meta:
        model = employee
        fields = "__all__"
        widgets = {
            'date':forms.DateInput(
                attrs = {
                    'type':'date'
                }
                
            )
        }
        
