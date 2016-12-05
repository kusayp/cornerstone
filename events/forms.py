from django import forms

from .models import Register

class RegisterForm(forms.ModelForm):
	class Meta:
		model = Register 
		fields = ['name', 'email', 'phone']  
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'onFocus': "this.value=''", 'name':'name', 'required': 'true', 'placeholder': 'Your Name'}), 
            'email': forms.TextInput(attrs={'class': 'form-control', 'onFocus': "this.value=''", 'name':'email', 'required': 'true', 'placeholder': 'Your Email', 'type' : 'email'}), 
            'phone': forms.TextInput(attrs={'class': 'form-control', 'onFocus': "this.value=''", 'name':'phone', 'required': 'true', 'placeholder': 'Your Mobile Number'}),
        }