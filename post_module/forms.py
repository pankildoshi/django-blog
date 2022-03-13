from dataclasses import fields
from turtle import width
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'headline': forms.TextInput(attrs={'placeholder': 'Post Headline'}),
            'content': forms.Textarea(attrs={'placeholder': 'Comtent'}),
        }