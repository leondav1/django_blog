from django import forms

from .models import Post, PostComment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'active']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['name', 'user', 'comment']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'id': 'contactcomment'}),
        }
