from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
		'first_name', 'last_name', 'email', 'password'
	    ]
        widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'email': forms.TextInput(),
            'password': forms.TextInput(attrs={'type':'password'}),
        }