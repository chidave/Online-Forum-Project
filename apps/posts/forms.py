from django.forms import ModelForm
from django.utils.translation import gettext_lazy

from .models import Post, Comment


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a title for your post', 'aria-label': 'Title of your post'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write something...', 'aria-label': 'Body of your post'})

    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write a comment...', 'aria-label': 'Write your comment'})

    class Meta:
        model = Comment
        fields = ['content']