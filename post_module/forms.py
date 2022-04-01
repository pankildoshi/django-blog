from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
        'title', 'headline', 'content', 'author', 'featured_image'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'headline': forms.TextInput(attrs={'placeholder': 'Post Headline'}),
            'content': forms.Textarea(attrs={'placeholder': 'Content'}),
            'author': forms.TextInput(attrs={'value': '', 'id':'author', 'type':'hidden'}),
        }