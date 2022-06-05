from django import forms
from django.db import models

from blog.models import Post,Comment

class PostForm(forms.ModelForm):
    title=forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model=Post
        fields=('title','content','image','category')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        labels={"body":"new"}