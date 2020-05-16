from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
    # post itself
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Title here'}))
    author = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Author name here'}))
    body = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Text here'}))
    
    # personal info
    email = forms.EmailField()
    address = forms.CharField(required=False)

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'body',
            'email',
            'address',
        ]