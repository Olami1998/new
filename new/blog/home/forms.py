from .models import Comment, Post
from django import forms


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'images', 'status']
        labels = {'title': 'Title', 'slug': 'Slug', 'content': 'Content', 'images': 'images', 'status': 'status'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        
        
