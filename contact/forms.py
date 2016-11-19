from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'phone', 'content'] 
		widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your Name', 'id': 'name'}), 
            'email': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your Email', 'id': 'email'}), 
            'phone': forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'placeholder': 'Your Mobile Number', 'id': 'phone'}), 
            'content': forms.Textarea(attrs={'class': 'form-control', 'required': 'true', 'rows': '3=6', 'placeholder': 'Your Message', 'id': 'content'}),
        }
