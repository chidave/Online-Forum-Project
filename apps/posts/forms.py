from django.forms import ModelForm
from django.utils.translation import gettext_lazy

from .models import Post


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter a title for your post'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Write something...'})

    class Meta:
        model = Post
        fields = ['title', 'content']