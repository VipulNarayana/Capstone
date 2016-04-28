from django import forms
from django.forms import TextInput
from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model=User
		fields=['email',]
		labels={
		'email':''
		} 
		widgets = {
            'email': TextInput(attrs={'size':'50','required':True,'class':'form-control','placeholder':'Email Address'}),
        }
