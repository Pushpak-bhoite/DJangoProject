from django.core import validators
from django import forms
from .models import User

class StudentRegistration(forms.ModelForm) :
    class Meta:
        model = User
        fields = ['emp_name','email','work']
        widgets = {
            #These included classes use to add css to form
            'emp_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'work': forms.TextInput(attrs={'class':'form-control'}),
        }

 