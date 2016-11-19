from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'required': 'true', 'id':'login-username-inline', 'data-parsley-trigger': 'keyup', 'data-parsley-minlength':'6', 'data-parsley-validation-threshold':'5', 'data-parsley-minlength-message':'Login should be at least 6 chars'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'required': 'true', 'id': 'login-password-inline'}))