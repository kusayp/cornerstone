from django import forms

from .models import Comment 

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['author', 'content'] 
		widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'onFocus': "this.value=''", 'required': 'true', 'name' : 'author', 'id' : 'comment-name', 'placeholder': 'Your Name', }), 
            'content': forms.Textarea(attrs={'class': 'form-control', 'onFocus': "this.value=''", 'required': 'true', 'name' : 'content', 'rows': '3=6', 'placeholder': 'Your Message', 'id' : 'comment-message'}),
        }