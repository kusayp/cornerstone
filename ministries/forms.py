from django import forms

from .models import Donation

class DonationForm(forms.ModelForm):
	class Meta:
		model = Donation 
		fields = ['firstname', 'lastname', 'email', 'phone', 'city', 'address', 'ministry', 'amount']  
		widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'First Name'}), 
            'lastname': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Last Name'}), 
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your E-Mail'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your Mobile Number'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your City'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your Box Number'}),
            'ministry': forms.Select(attrs={'class': 'form-control', 'required': 'true', 'placeholder':'Select a Minitry to Donate to'}),
            'amount': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Amount to Donate'}),
        }