# forms.py
from .models import Post, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title', 'car_model', 'production_year', 'price', 'content', 'excerpt']