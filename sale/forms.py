# forms.py
from .models import Post, Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class CommentAdminForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', 'approved')

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title', 'car_model', 'production_year', 'price', 'content', 'excerpt']

class PostAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(PostAdminForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Post
        fields = ['title', 'car_model', 'production_year', 'price', 'status', 'content', 'excerpt']